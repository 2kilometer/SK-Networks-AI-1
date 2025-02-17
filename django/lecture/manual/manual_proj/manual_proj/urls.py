"""
URL configuration for manual_proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from orders.entity import orders

urlpatterns = [
    path('admin/', admin.site.urls),
    # board Domain으로 요청이 들어가는 모든 것을
    # board 디렉토리 하위의 urls.py에서 관리하겠다는 의미
    path('board/', include('board.urls')),
    path('product/', include('product.urls')),
    path('oauth/', include('oauth.urls')),
    path('account/', include('account.urls')),
    path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls')),
    path('survey/', include('survey.urls')),
    path('backlog/', include('backlog.urls')),
    path('backlog-status/', include('backlog_status.urls')),
    path('backlog-domain/', include('backlog_domain.urls')),
    path('backlog-success-criteria/', include('backlog_success_criteria.urls')),
    path('backlog-map-number/', include('backlog_map_number.urls')),
    path('backlog-review/', include('backlog_review.urls')),
    path('backlog-issue/', include('backlog_issue.urls')),
    path('ai-request/', include('ai_request.urls')),
]
