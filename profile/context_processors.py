import datetime
from datetime import timedelta

from django.db.models import Avg, Count, Min, Q, Sum
from django.shortcuts import redirect, render
from django.utils import timezone

from notification.models import Notification, PrivRepNotification
from qa.models import Question


def top_questions(request):
    questionsHome = Question.objects.filter(
        is_deleted=False, is_bountied=False
    ).order_by("-date")[:50]
    return {"questionsHome": questionsHome}


def count_all_bounties(request):
    bounties = Question.objects.filter(is_bountied=True)

    return {"count_bounty": bounties.count()}
