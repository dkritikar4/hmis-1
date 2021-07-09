import json
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.core import serializers
from django.core.serializers import serialize
from django.db.models import Q
from dashboard.models import AreaDetails, HmisPw, HmisChldImmunzt, HmisChldDisease
from django.core.serializers.json import DjangoJSONEncoder 

from .models import (PieState, PieChldDisease, PieChldImmunzt, GeojsonIndiaLevel)

# Create your views here.

class HMISDashboardView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/dash_base.html"
    

class hmisBarChart(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request, fy= None, dist_name = None):
        district = request.GET.get('dist_name', dist_name) 
        fy_name = request.GET.get('fy', fy) 
        if district == '22': 
            data = list(HmisPw.objects.filter(Q(financial_year=fy_name) & Q(area_parent_id=22)).values())
            
        else:    
            data = list(HmisPw.objects.filter(Q(financial_year=fy_name) & Q(area_parent_id=1)).values())

        for i in data:
            area_n = AreaDetails.objects.filter(Q(area_id = i['area_id'])).values('area_name')
            i.update(area_n[0])

        jsondata = json.dumps(data, cls=DjangoJSONEncoder)
        
        return render(request,'hmis_dash/barchart.html', {'data':jsondata, 'fy': fy_name, 'dist_name': district})


class hmisLineChart(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request,fy=None):
        fy_name = request.GET.get('fy', fy) 
        data = HmisStatePw.objects.filter(Q(year=fy_name)).order_by('month').exclude(month='All')
        st_name = HmisStatePw.objects.values('state').distinct().order_by('state')
        jsondata = serializers.serialize('json',data)

        return render(request,'hmis_dash/linechart.html', {'data':jsondata, 'fy': fy_name, 'state':st_name})


class fyLine(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request,fy=None, dist_name = None):
        district = request.GET.get('dist_name', dist_name) 
        fy_name = request.GET.get('fy', fy) 
        data = HmisStatePw.objects.all().order_by('month').exclude(month='All')
        st_name = HmisStatePw.objects.values('state').distinct().order_by('state')
        fyList = HmisStatePw.objects.values('year').distinct().order_by('year')
        jsondata = serializers.serialize('json',data)

        return render(request,'hmis_dash/fy_line.html', {'data':jsondata, 'fy': fy_name, 'fyList':fyList, 'dist_name': district, 'state':st_name})


class fyLineNum(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request,fy=None, dist_name = None):
        district = request.GET.get('dist_name', dist_name) 
        fy_name = request.GET.get('fy', fy) 
        data = HmisStatePw.objects.all().order_by('month').exclude(month='All')
        st_name = HmisStatePw.objects.values('state').distinct().order_by('state')
        fyList = HmisStatePw.objects.values('year').distinct().order_by('year')
        jsondata = serializers.serialize('json',data)

        return render(request,'hmis_dash/fy_lineNum.html', {'data':jsondata, 'fy': fy_name, 'fyList':fyList, 'dist_name': district, 'state':st_name})


class hmisBarNumericChart(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request, fy= None, dist_name = None):
        district = request.GET.get('dist_name', dist_name) 
        fy_name = request.GET.get('fy', fy) 
        data = HmisPw.objects.filter(Q(financial_year=fy_name)).exclude(area_id=1)
        jsondata = serializers.serialize('json', data)
        
        return render(request,'hmis_dash/barNumericChart.html', {'data':jsondata, 'fy': fy_name, 'dist_name': district})


class hmisLineNumericChart(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request,fy=None):
        fy_name = request.GET.get('fy', fy) 
        data = HmisStatePw.objects.filter(Q(year=fy_name)).order_by('month').exclude(month='All')
        st_name = HmisStatePw.objects.values('state').distinct().order_by('state')
        jsondata = serializers.serialize('json',data)

        return render(request,'hmis_dash/lineNumericChart.html', {'data':jsondata, 'fy': fy_name, 'state':st_name})


class chldImmuBar(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request, fy= None, dist_name = None):
        district = request.GET.get('dist_name', dist_name) 
        fy_name = request.GET.get('fy', fy) 
        data = HmisStChldImmunzt.objects.filter(Q(year=fy_name)).exclude(state='All States')
        jsondata = serializers.serialize('json', data)
        
        return render(request,'hmis_dash/chldImmuBar.html', {'data':jsondata, 'fy': fy_name, 'dist_name': district})


class chldImmuLine(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request,fy=None):
        fy_name = request.GET.get('fy', fy) 
        data = HmisStChldImmunzt.objects.filter(Q(year=fy_name)).order_by('month').exclude(month='All')
        st_name = HmisStChldImmunzt.objects.values('state').distinct().order_by('state')
        jsondata = serializers.serialize('json',data)

        return render(request,'hmis_dash/chldImmuLine.html', {'data':jsondata, 'fy': fy_name, 'state':st_name})


class chldImmuBarNumeric(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request, fy= None, dist_name = None):
        district = request.GET.get('dist_name', dist_name) 
        fy_name = request.GET.get('fy', fy) 
        data = HmisStChldImmunzt.objects.filter(Q(year=fy_name)).exclude(state='All States')
        jsondata = serializers.serialize('json', data)
        
        return render(request,'hmis_dash/chldImmuBarNumeric.html', {'data':jsondata, 'fy': fy_name, 'dist_name': district})


class chldImmuLineNumeric(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request,fy=None):
        fy_name = request.GET.get('fy', fy) 
        data = HmisStChldImmunzt.objects.filter(Q(year=fy_name)).order_by('month').exclude(month='All')
        st_name = HmisStChldImmunzt.objects.values('state').distinct().order_by('state')
        jsondata = serializers.serialize('json',data)

        return render(request,'hmis_dash/chldImmuLineNumeric.html', {'data':jsondata, 'fy': fy_name, 'state':st_name})


class chldDiseaseBar(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request, fy= None, dist_name = None):
        district = request.GET.get('dist_name', dist_name) 
        fy_name = request.GET.get('fy', fy) 
        data = HmisStChldDisease.objects.filter(Q(year=fy_name)).exclude(state='All States')
        jsondata = serializers.serialize('json', data)
        
        return render(request,'hmis_dash/chldDiseaseBar.html', {'data':jsondata, 'fy': fy_name, 'dist_name': district})


class chldDiseaseLine(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request,fy=None):
        fy_name = request.GET.get('fy', fy) 
        data = HmisStChldDisease.objects.filter(Q(year=fy_name)).order_by('month').exclude(month='All')
        st_name = HmisStChldDisease.objects.values('state').distinct().order_by('state')
        jsondata = serializers.serialize('json',data)

        return render(request,'hmis_dash/chldDiseaseLine.html', {'data':jsondata, 'fy': fy_name, 'state':st_name})


class chldDiseaseBarNumeric(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request, fy= None, dist_name = None):
        district = request.GET.get('dist_name', dist_name) 
        fy_name = request.GET.get('fy', fy) 
        data = HmisStChldDisease.objects.filter(Q(year=fy_name)).exclude(state='All States')
        jsondata = serializers.serialize('json', data)
        
        return render(request,'hmis_dash/chldDiseaseBarNumeric.html', {'data':jsondata, 'fy': fy_name, 'dist_name': district})


class chldDiseaseLineNumeric(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request,fy=None):
        fy_name = request.GET.get('fy', fy) 
        data = HmisStChldDisease.objects.filter(Q(year=fy_name)).order_by('month').exclude(month='All')
        st_name = HmisStChldDisease.objects.values('state').distinct().order_by('state')
        jsondata = serializers.serialize('json',data)

        return render(request,'hmis_dash/chldDiseaseLineNumeric.html', {'data':jsondata, 'fy': fy_name, 'state':st_name})

    
class hmisTableChart(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request,fy=None, dist_name = None):
        district = request.GET.get('dist_name', dist_name) 
        print(district)
        fy_name = request.GET.get('fy', fy) 
        if district == '22': 
            pw_data = list(HmisPw.objects.filter(Q(financial_year=fy_name) & Q(area_parent_id=22)).values())
            childIm_data = list(HmisChldImmunzt.objects.filter(Q(financial_year=fy_name) & Q(area_parent_id=22)).values())
            childDi_data = list(HmisChldDisease.objects.filter(Q(financial_year=fy_name) & Q(area_parent_id=22)).values())
            # area_list = AreaDetails.objects.filter(Q(area_parent_id=22)).values('area_name').distinct().order_by('area_id')
        else:
            pw_data = list(HmisPw.objects.filter(Q(financial_year=fy_name) & Q(area_parent_id=1)).values())
            childIm_data = list(HmisChldImmunzt.objects.filter(Q(financial_year=fy_name) & Q(area_parent_id=1)).values())
            childDi_data = list(HmisChldDisease.objects.filter(Q(financial_year=fy_name) & Q(area_parent_id=1)).values())
            # area_list = AreaDetails.objects.filter(Q(area_parent_id=1)).values('area_name').distinct().order_by('area_id')

        for i in pw_data:
            area_n = AreaDetails.objects.filter(Q(area_id = i['area_id'])).values('area_name')
            i.update(area_n[0])

        for i in childIm_data:
            area_n = AreaDetails.objects.filter(Q(area_id = i['area_id'])).values('area_name')
            i.update(area_n[0])   

        for i in childDi_data:
            area_n = AreaDetails.objects.filter(Q(area_id = i['area_id'])).values('area_name')
            i.update(area_n[0])  

        json_childIm_data = json.dumps(childIm_data, cls=DjangoJSONEncoder)
        json_childDi_data = json.dumps(childDi_data, cls=DjangoJSONEncoder)
        jsonpw_data = json.dumps(pw_data, cls=DjangoJSONEncoder)

        context = {
            'chilIm_data': json_childIm_data,
            'childDi_data': json_childDi_data,
            'pw_data': jsonpw_data
        }

        return render(request,'hmis_dash/tableOverview.html', {'context':context, 'fy': fy_name, 'dist_name': district})


class pieStateLevel(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request, fy= None):
        fy_name = request.GET.get('fy', fy) 
        data = PieState.objects.filter(Q(year=fy_name))
        jsondata = serializers.serialize('json', data)

        return render(request,'hmis_dash/piechart_stlvl.html', {'data':jsondata, 'fy': fy_name})


class pieChildImmu(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request, fy= None):
        fy_name = request.GET.get('fy', fy) 
        data = PieChldImmunzt.objects.filter(Q(year=fy_name))
        jsondata = serializers.serialize('json', data)

        return render(request,'hmis_dash/pieChldImmu.html', {'data':jsondata, 'fy': fy_name})


class pieChildDisease(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request, fy= None):
        fy_name = request.GET.get('fy', fy) 
        data = PieChldDisease.objects.filter(Q(year=fy_name))
        jsondata = serializers.serialize('json', data)

        return render(request,'hmis_dash/pieChldDisease.html', {'data':jsondata, 'fy': fy_name})


class mapStPW(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request,fy=None):
        fy_name = request.GET.get('fy', fy) 
        st_data = HmisStatePw.objects.filter(Q(year=fy_name)).exclude(state='All States')
        
        st_jsondata = serializers.serialize('json', st_data)
        
        st_geodata = serialize('geojson', GeojsonIndiaLevel.objects.all(),
                                geometry_field = 'wkb_geometry',
                                fields = ('ogc_fid','state'))
        
        context = {
            'st_data': st_jsondata,
            'st_geodata': st_geodata
        }

        return render(request,'hmis_dash/mapPW.html', {'context':context, 'fy': fy_name})


class mapStChldImmu(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request,fy=None):
        fy_name = request.GET.get('fy', fy) 
        st_data = HmisStChldImmunzt.objects.filter(Q(year=fy_name)).exclude(state='All States')
        
        st_jsondata = serializers.serialize('json', st_data)
        
        st_geodata = serialize('geojson', GeojsonIndiaLevel.objects.all(),
                                geometry_field = 'wkb_geometry',
                                fields = ('ogc_fid','state'))
        
        context = {
            'st_data': st_jsondata,
            'st_geodata': st_geodata
        }

        return render(request,'hmis_dash/mapChldImmu.html', {'context':context, 'fy': fy_name})


class mapStChldDisease(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request,fy=None):
        fy_name = request.GET.get('fy', fy) 
        st_data = HmisStChldDisease.objects.filter(Q(year=fy_name)).exclude(state='All States')
        
        st_jsondata = serializers.serialize('json', st_data)
        
        st_geodata = serialize('geojson', GeojsonIndiaLevel.objects.all(),
                                geometry_field = 'wkb_geometry',
                                fields = ('ogc_fid','state'))
        
        context = {
            'st_data': st_jsondata,
            'st_geodata': st_geodata
        }

        return render(request,'hmis_dash/mapChldDisease.html', {'context':context, 'fy': fy_name})


class fyChldImmuLine(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request,fy=None, dist_name = None):
        district = request.GET.get('dist_name', dist_name) 
        fy_name = request.GET.get('fy', fy) 
        data = HmisStChldImmunzt.objects.all().order_by('month').exclude(month='All')
        st_name = HmisStChldImmunzt.objects.values('state').distinct().order_by('state')
        fyList = HmisStChldImmunzt.objects.values('year').distinct().order_by('year')
        jsondata = serializers.serialize('json',data)

        return render(request,'hmis_dash/fy_ci_line.html', {'data':jsondata, 'fy': fy_name, 'fyList':fyList, 'dist_name': district, 'state':st_name})


class fyChldImmuLineNum(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request,fy=None, dist_name = None):
        district = request.GET.get('dist_name', dist_name) 
        fy_name = request.GET.get('fy', fy) 
        data = HmisStChldImmunzt.objects.all().order_by('month').exclude(month='All')
        st_name = HmisStChldImmunzt.objects.values('state').distinct().order_by('state')
        fyList = HmisStChldImmunzt.objects.values('year').distinct().order_by('year')
        jsondata = serializers.serialize('json',data)

        return render(request,'hmis_dash/fy_ci_lineNum.html', {'data':jsondata, 'fy': fy_name, 'fyList':fyList, 'dist_name': district, 'state':st_name})


class fyChldDiseaseLine(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request,fy=None, dist_name = None):
        district = request.GET.get('dist_name', dist_name) 
        fy_name = request.GET.get('fy', fy) 
        data = HmisStChldDisease.objects.all().order_by('month').exclude(month='All')
        st_name = HmisStChldDisease.objects.values('state').distinct().order_by('state')
        fyList = HmisStChldDisease.objects.values('year').distinct().order_by('year')
        jsondata = serializers.serialize('json',data)

        return render(request,'hmis_dash/fy_cd_line.html', {'data':jsondata, 'fy': fy_name, 'fyList':fyList, 'dist_name': district, 'state':st_name})


class fyChldDiseaseLineNum(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request,fy=None, dist_name = None):
        district = request.GET.get('dist_name', dist_name) 
        fy_name = request.GET.get('fy', fy) 
        data = HmisStChldDisease.objects.all().order_by('month').exclude(month='All')
        st_name = HmisStChldDisease.objects.values('state').distinct().order_by('state')
        fyList = HmisStChldDisease.objects.values('year').distinct().order_by('year')
        jsondata = serializers.serialize('json',data)

        return render(request,'hmis_dash/fy_cd_lineNum.html', {'data':jsondata, 'fy': fy_name, 'fyList':fyList, 'dist_name': district, 'state':st_name})