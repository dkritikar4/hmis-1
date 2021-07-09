"""hmis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from dashboard.views import DashboardView, RegionOverview
from hmis_dash.views import (HMISDashboardView, hmisBarChart, hmisLineChart, hmisBarNumericChart, hmisLineNumericChart,
    chldImmuBar, chldImmuLine, chldImmuBarNumeric, chldImmuLineNumeric, chldDiseaseBar, chldDiseaseLine, chldDiseaseBarNumeric,
    chldDiseaseLineNumeric, hmisTableChart, pieStateLevel, pieChildDisease, pieChildImmu,mapStPW, mapStChldImmu, mapStChldDisease,
    fyLine, fyLineNum, fyChldImmuLine, fyChldImmuLineNum, fyChldDiseaseLine, fyChldDiseaseLineNum)
from django.conf import settings
from django.conf.urls.static import static
from dashboard import views

urlpatterns = [
    url(r'^$', DashboardView.as_view(), name='home'),
    url(r'^dashboard/$', RegionOverview.as_view(), name='overview'),
    url(r'^(?P<fy>[-\w\ ]+)/dashboard/ajax/areaChange/$', views.create_post_area, name='ajaxArea'),    
    
    url(r'^hmis_dash$', HMISDashboardView.as_view(), name='hmis_dash'),
    url(r'^(?P<dist_name>[-\w]+)/(?P<fy>[-\w\ ]+)/hmis_dash/barchart$', hmisBarChart.as_view(), name='barchart'),
    url(r'^(?P<dist_name>[-\w]+)/(?P<fy>[-\w\ ]+)/hmis_dash/fy_line$', fyLine.as_view(), name='fy_line'),
    url(r'^(?P<dist_name>[-\w]+)/(?P<fy>[-\w\ ]+)/hmis_dash/fy_lineNum$', fyLineNum.as_view(), name='fy_lineNum'),
    url(r'^(?P<dist_name>[-\w]+)/(?P<fy>[-\w\ ]+)/hmis_dash/linechart$', hmisLineChart.as_view(), name='linechart'),
    url(r'^(?P<dist_name>[-\w]+)/(?P<fy>[-\w\ ]+)/hmis_dash/barnumeric$', hmisBarNumericChart.as_view(), name='barnumeric'),
    url(r'^(?P<dist_name>[-\w]+)/(?P<fy>[-\w\ ]+)/hmis_dash/linenumeric$', hmisLineNumericChart.as_view(), name='linenumeric'),

    url(r'^(?P<dist_name>[-\w]+)/(?P<fy>[-\w\ ]+)/hmis_dash/ci_bar$', chldImmuBar.as_view(), name='ci_bar'),
    url(r'^(?P<fy>[-\w\ ]+)/hmis_dash/ci_line$', chldImmuLine.as_view(), name='ci_line'),
    url(r'^(?P<dist_name>[-\w]+)/(?P<fy>[-\w\ ]+)/hmis_dash/ci_barnumeric$', chldImmuBarNumeric.as_view(), name='ci_barnumeric'),
    url(r'^(?P<fy>[-\w\ ]+)/hmis_dash/ci_linenumeric$', chldImmuLineNumeric.as_view(), name='ci_linenumeric'),
    
    url(r'^(?P<dist_name>[-\w]+)/(?P<fy>[-\w\ ]+)/hmis_dash/cd_bar$', chldDiseaseBar.as_view(), name='cd_bar'),
    url(r'^(?P<fy>[-\w\ ]+)/hmis_dash/cd_line$', chldDiseaseLine.as_view(), name='cd_line'),
    url(r'^(?P<dist_name>[-\w]+)/(?P<fy>[-\w\ ]+)/hmis_dash/cd_barnumeric$', chldDiseaseBarNumeric.as_view(), name='cd_barnumeric'),
    url(r'^(?P<fy>[-\w\ ]+)/hmis_dash/cd_linenumeric$', chldDiseaseLineNumeric.as_view(), name='cd_linenumeric'),

    url(r'^(?P<dist_name>[-\w]+)/(?P<fy>[-\w\ ]+)/hmis_dash/tableOverview$', hmisTableChart.as_view(), name='tablechart'),
    url(r'^(?P<dist_name>[-\w]+)/(?P<fy>[-\w\ ]+)/hmis_dash/stlvl_pie$', pieStateLevel.as_view(), name='stlvl_pie'),
    url(r'^(?P<fy>[-\w\ ]+)/hmis_dash/ci_pie$', pieChildImmu.as_view(), name='ci_pie'),
    url(r'^(?P<fy>[-\w\ ]+)/hmis_dash/cd_pie$', pieChildDisease.as_view(), name='cd_pie'),

    url(r'^(?P<fy>[-\w\ ]+)/hmis_dash/pw_map$', mapStPW.as_view(), name='pw_map'),
    url(r'^(?P<fy>[-\w\ ]+)/hmis_dash/cd_map$', mapStChldDisease.as_view(), name='ci_map'),
    url(r'^(?P<fy>[-\w\ ]+)/hmis_dash/ci_map$', mapStChldImmu.as_view(), name='cd_map'),

    url(r'^(?P<dist_name>[-\w]+)/(?P<fy>[-\w\ ]+)/hmis_dash/fy_ci_line$', fyChldImmuLine.as_view(), name='fy_ci_line'),
    url(r'^(?P<dist_name>[-\w]+)/(?P<fy>[-\w\ ]+)/hmis_dash/fy_ci_lineNum$', fyChldImmuLineNum.as_view(), name='fy_ci_lineNum'),

    url(r'^(?P<dist_name>[-\w]+)/(?P<fy>[-\w\ ]+)/hmis_dash/fy_cd_line$', fyChldDiseaseLine.as_view(), name='fy_cd_line'),
    url(r'^(?P<dist_name>[-\w]+)/(?P<fy>[-\w\ ]+)/hmis_dash/fy_cd_lineNum$', fyChldDiseaseLineNum.as_view(), name='fy_cd_lineNum'),


    url(r'^admin/', admin.site.urls),
    url(r'^login/', views.login_request, name='login'),
    url(r'^logout/', views.logout_request, name='logout'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)