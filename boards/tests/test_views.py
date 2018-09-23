from django.contrib.auth.models import User
from django.urls import reverse, resolve
from django.test import TestCase
from ..views import new_topic
from ..models import Board, Topic, Post
from ..forms import NewTopicForm
