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
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render

from .models import Notification, PrivRepNotification


def notificationViewer(request):
    if request.user.is_authenticated:
        notifications = Notification.objects.filter(
            noti_receiver=request.user
        ).order_by("-date_created")
        countUnreadNotifications = Notification.objects.filter(
            noti_receiver=request.user, is_read=False
        ).count()
        if countUnreadNotifications >= 1:
            showAlert = True
        else:
            showAlert = False

    else:
        notifications = ""
        countUnreadNotifications = ""
        showAlert = False

    return {
        "notifications": notifications,
        "countUnreadNotifications": countUnreadNotifications,
        "showAlert": showAlert,
    }


def privNotificationViewer(request):
    if request.user.is_authenticated:
        privNotifications = PrivRepNotification.objects.filter(
            for_user=request.user
        ).order_by("-date_created_PrivNotify")
        countUnreadPrivNotifications_1 = PrivRepNotification.objects.filter(
            for_user=request.user, is_read=False
        ).count()
        countUnreadPrivNotifications = PrivRepNotification.objects.filter(
            for_user=request.user, is_read=False
        ).aggregate(countTheUnRead_Rep=Sum("missingReputation"))
        # if countUnreadPrivNotifications >= 1:
        # 	showPrivAlert = True
        # else:
        # 	showPrivAlert = False

    else:
        privNotifications = ""
        countUnreadPrivNotifications = ""
        # showPrivAlert = False
        countUnreadPrivNotifications_1 = ""

    return {
        "privNotifications": privNotifications,
        "countUnreadPrivNotifications": countUnreadPrivNotifications,
        "countUnreadPrivNotifications_1": countUnreadPrivNotifications_1,
    }
