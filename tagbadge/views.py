import datetime
from datetime import timedelta

from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from taggit.models import Tag

from qa.models import Question

from .models import TagBadge


def badges(request):
    tags = TagBadge.objects.filter(preBuild=True).exclude(awarded_to_user__isnull=False)

    recentsEarned_badges = TagBadge.objects.filter(preBuild=False).order_by("-date")

    context = {"tags": tags, "recentsEarned_badges": recentsEarned_badges}
    return render(request, "tagbadge/badges.html", context)


# It will show only tags which are posted by user_id
def taggedItems(request, tag_id, user_id):
    tag = Tag.objects.get(id=tag_id)

    getAllQuestions = Question.objects.filter(post_owner=user_id, tags=tag)

    context = {
        "tag": tag,
        "getAllQuestions": getAllQuestions,
    }
    return render(request, "profile/taggedItems_ofUser.html", context)


def taggedItemsFrom_All(request, tag_id):
    tag = Tag.objects.get(id=tag_id)

    questions = Question.objects.filter(tags=tag)

    context = {"tag": tag, "questions": questions, "count_questions": questions.count()}
    return render(request, "qa/taggedItemsFrom_All.html", context)
