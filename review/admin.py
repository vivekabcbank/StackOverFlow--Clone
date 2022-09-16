from django.contrib import admin

# from .models import QuestionEdit
from .models import (
    CloseQuestionVotes,
    FirstAnswerReview,
    FirstQuestionReview,
    FlagComment,
    FlagPost,
    LateAnswerReview,
    LowQualityPostsCheck,
    QuestionEditVotes,
    ReOpenQuestionVotes,
    ReviewCloseVotes,
    ReviewFlagComment,
    ReviewFlagPost,
    ReviewLowQualityPosts,
    ReviewQuestionEdit,
    ReviewQuestionReOpenVotes,
)

# admin.site.register(QuestionEdit)

admin.site.register(FirstAnswerReview)

admin.site.register(FirstQuestionReview)

admin.site.register(LateAnswerReview)

admin.site.register(CloseQuestionVotes)

admin.site.register(ReviewCloseVotes)

admin.site.register(ReOpenQuestionVotes)

admin.site.register(ReviewQuestionReOpenVotes)

admin.site.register(QuestionEditVotes)

admin.site.register(ReviewQuestionEdit)

admin.site.register(LowQualityPostsCheck)

admin.site.register(ReviewLowQualityPosts)

admin.site.register(FlagComment)

admin.site.register(ReviewFlagPost)

admin.site.register(ReviewFlagComment)

admin.site.register(FlagPost)
