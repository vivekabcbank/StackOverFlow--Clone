from django import template
from django.db.models import (
    Avg,
    BooleanField,
    Case,
    Count,
    Exists,
    ExpressionWrapper,
    F,
    FloatField,
    IntegerField,
    Max,
    Min,
    OuterRef,
    Q,
    Sum,
    Value,
    When,
)

from qa.models import Reputation
from tagbadge.models import TagBadge

register = template.Library()


@register.filter
def calculateEarned_Badge_Users(tag):
    counting = TagBadge.objects.filter(id=tag).aggregate(Sum("awarded_to_user"))
    return counting
