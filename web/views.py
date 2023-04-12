import time
from django.views.decorators.clickjacking import xframe_options_exempt

from taskSource.run_views import run_views
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from web.models import AdsTask
from web.models import BitTask


def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username == "cc" and password == "123":
            return render(request, 'task_status.html')
        else:
            return HttpResponse("登录失败！")
    return render(request, 'index.html')


def adspower(request):
    return render(request, 'adspower.html')


def bitbrowser(request):
    return render(request, 'bitbrowser.html')


def others(request):
    return render(request, 'others.html')


@xframe_options_exempt
def list(request):
    nowDate = time.strftime('%Y-%m-%d')
    date = request.GET.get('start_time')
    if date is None:
        date = time.strftime('%Y-%m-%d')
    date_list = AdsTask.objects.filter(dayTime=date).all()
    return render(request, 'task_list.html', {'data_list': date_list, 'date': date, 'nowDate': nowDate})


@xframe_options_exempt
def bitlist(request):
    nowDate = time.strftime('%Y-%m-%d')
    bitDate = request.GET.get('bit_time')
    if bitDate is None:
        bitDate = nowDate
    bit_list = BitTask.objects.filter(dayTime=bitDate).all()
    return render(request, 'bit_list.html', {'bit_list': bit_list, 'bitDate': bitDate, 'nowDate': nowDate})


@xframe_options_exempt
def othersAds(request):
    nowDate = time.strftime('%Y-%m-%d')
    adsDate = request.GET.get('start_time')
    if adsDate is None:
        adsDate = nowDate
    ads_list = AdsTask.objects.filter(dayTime=adsDate).all()
    return render(request, 'others_ads.html', {'ads_list': ads_list, 'adsDate': adsDate, 'nowDate': nowDate})


@xframe_options_exempt
def othersBit(request):
    nowDate = time.strftime('%Y-%m-%d')
    bitDate = request.GET.get('start_time')
    if bitDate is None:
        bitDate = nowDate
    bit_list = BitTask.objects.filter(dayTime=bitDate).all()
    return render(request, 'others_bit.html', {'bit_list': bit_list, 'bitDate': bitDate, 'nowDate': nowDate})


def status(request):
    nowDate = time.strftime('%Y-%m-%d')
    date = request.GET.get('start_time')
    if date is None:
        date = nowDate
    allTask = AdsTask.objects.filter(dayTime=date).all()

    # carv任务判断成功数和失败数
    carvSuccess = AdsTask.objects.filter(Q(Carv__contains="成功") & Q(dayTime=date)).all()
    carvFail = AdsTask.objects.filter(Q(Carv__contains="失败") & Q(dayTime=date) | Q(Carv=None) & Q(dayTime=date)).all()

    # CoinMarketcap任务判断成功数和失败数
    CMCSuccess = AdsTask.objects.filter(Q(Coinmarketcap__contains="成功") & Q(dayTime=date) | Q(Coinmarketcap__contains="已经") & Q(dayTime=date)).all()
    CMCFail = AdsTask.objects.filter(
        Q(Coinmarketcap__contains="失败") & Q(dayTime=date) | Q(Coinmarketcap=None) & Q(dayTime=date)).all()

    # CoinGecko任务判断成功数和失败数
    CGKSuccess = AdsTask.objects.filter(
        Q(Coingecko__contains="分钟前") & Q(dayTime=date) | Q(Coingecko__contains="下次") & Q(dayTime=date)).all()
    CGKFail = AdsTask.objects.filter(
        Q(Coingecko__contains="天前") & Q(dayTime=date) | Q(Coingecko__contains="24 小时") & Q(dayTime=date) | Q(Coingecko=None) & Q(dayTime=date)).all()

    # Zetalabs任务判断成功数和失败数
    ZetaSuccess = AdsTask.objects.filter(Q(Zetalabs__contains="swap") & Q(dayTime=date)).all()
    ZetaToken = AdsTask.objects.filter(Q(Zetalabs__contains="测试币") & Q(dayTime=date)).all()
    ZetaFail = AdsTask.objects.filter(Q(Zetalabs=None) & Q(dayTime=date)).all() | AdsTask.objects.filter(
        Q(Zetalabs__contains="You will receive") & Q(dayTime=date)).all() | AdsTask.objects.filter(
        Q(Zetalabs__contains="失败") & Q(dayTime=date)).all()

    # Cassava任务判断成功数和失败数
    CassavaSuccess = AdsTask.objects.filter(
        Q(Cassava__contains="成功") & Q(dayTime=date) | Q(Cassava__contains="today") & Q(dayTime=date)).all()
    CassavaFail = AdsTask.objects.filter(
        Q(Cassava=None) & Q(dayTime=date) | Q(Cassava__contains="失败") & Q(dayTime=date)).all()

    Layer3Success = AdsTask.objects.filter(Q(Layer3__contains="day gm") & Q(dayTime=date) | Q(Layer3__contains="还没") & Q(dayTime=date)).all()
    Layer3Fail = AdsTask.objects.filter(Q(Layer3=None) & Q(dayTime=date)).all()

    SoquestSuccess = AdsTask.objects.filter(Q(Soquest__contains="Tomorrow") & Q(dayTime=date)).all()
    SoquestFail = AdsTask.objects.filter(Q(Soquest=None) & Q(dayTime=date)).all()
    SoquestFailList = []
    for i in SoquestFail:
        if int(i.id) < 26:
            SoquestFailList.append(int(i.id))

    FusionistAll = AdsTask.objects.filter(Q(OtherTask3__contains=".") & Q(dayTime=date)).all()
    total = 0
    for i in FusionistAll:
        total = total + float(i.OtherTask3)

    allStatus = [
        len(allTask), len(carvSuccess), len(carvFail), len(CMCSuccess), len(CMCFail), len(CGKSuccess), len(CGKFail), len(ZetaSuccess), len(ZetaToken), len(ZetaFail), carvFail,
        CMCFail, CGKFail, ZetaFail, date, nowDate, len(CassavaSuccess), len(CassavaFail), CassavaFail, len(Layer3Success), len(Layer3Fail),
        Layer3Fail, len(SoquestSuccess), len(SoquestFail), SoquestFail, SoquestFailList, total
    ]

    return render(request, 'task_status.html', {'task_status': allStatus})

def bitstatus(request):
    nowDate = time.strftime('%Y-%m-%d')
    date = request.GET.get('bit_time')
    if date is None:
        date = nowDate
    allTask = BitTask.objects.filter(dayTime=date).all()

    # carv任务判断成功数和失败数
    carvSuccess = BitTask.objects.filter(Q(Carv__contains="成功") & Q(dayTime=date)).all()
    carvFail = BitTask.objects.filter(Q(Carv__contains="失败") & Q(dayTime=date) | Q(Carv=None) & Q(dayTime=date)).all()
    carvFailList = []
    for i in carvFail:
        if int(i.id) < 53:
            carvFailList.append(int(i.id))

    # CoinGecko任务判断成功数和失败数
    CGKSuccess = BitTask.objects.filter(
        Q(Coingecko__contains="分钟前") & Q(dayTime=date) | Q(Coingecko__contains="下次") & Q(dayTime=date)).all()
    CGKFail = BitTask.objects.filter(
        Q(Coingecko__contains="天前") & Q(dayTime=date) | Q(Coingecko__contains="24 小时") & Q(dayTime=date) | Q(Coingecko=None) & Q(dayTime=date)).all()

    # Zetalabs任务判断成功数和失败数
    ZetaSuccess = BitTask.objects.filter(Q(Zetalabs__contains="swap") & Q(dayTime=date)).all()
    ZetaToken = BitTask.objects.filter(Q(Zetalabs__contains="测试币") & Q(dayTime=date)).all()
    ZetaFail = BitTask.objects.filter(Q(Zetalabs=None) & Q(dayTime=date)).all() | BitTask.objects.filter(
        Q(Zetalabs__contains="You will receive") & Q(dayTime=date)).all() | BitTask.objects.filter(
        Q(Zetalabs__contains="失败") & Q(dayTime=date)).all()

    # CoinMarketcap任务判断成功数和失败数
    CMCSuccess = BitTask.objects.filter(Q(Coinmarketcap__contains="成功") & Q(dayTime=date) | Q(Coinmarketcap__contains="已经") & Q(dayTime=date)).all()
    CMCFail = BitTask.objects.filter(
        Q(Coinmarketcap__contains="失败") & Q(dayTime=date) | Q(Coinmarketcap=None) & Q(dayTime=date)).all()

    # Cassava任务判断成功数和失败数
    CassavaSuccess = BitTask.objects.filter(
        Q(Cassava__contains="成功") & Q(dayTime=date) | Q(Cassava__contains="today") & Q(dayTime=date)).all()
    CassavaFail = BitTask.objects.filter(
        Q(Cassava=None) & Q(dayTime=date) | Q(Cassava__contains="失败") & Q(dayTime=date)).all()

    Layer3Success = BitTask.objects.filter(Q(Layer3__contains="day gm") & Q(dayTime=date) | Q(Layer3__contains="还没") & Q(dayTime=date)).all()
    Layer3Fail = BitTask.objects.filter(Q(Layer3=None) & Q(dayTime=date)).all()

    FusionistAll = BitTask.objects.filter(Q(OtherTask3__contains=".") & Q(dayTime=date)).all()
    total = 0
    for i in FusionistAll:
        total = total + float(i.OtherTask3)

    allStatus = [
        len(allTask), len(carvSuccess), len(carvFail), len(CGKSuccess), len(CGKFail),
        len(ZetaSuccess), len(ZetaToken), len(ZetaFail),
        carvFail, CGKFail, ZetaFail, date, nowDate, len(CassavaSuccess), len(CassavaFail), CassavaFail, len(Layer3Success), len(Layer3Fail), Layer3Fail, carvFailList, total,
        len(CMCSuccess), len(CMCFail), CMCFail
    ]

    return render(request, 'bit_status.html', {'bit_status': allStatus})


def runTask(request):
    taskNum = request.GET.get('taskNum')
    carv = request.GET.get('carv')
    layer = request.GET.get('layer')
    ckg = request.GET.get('ckg')
    zeta = request.GET.get('zeta')
    cassava = request.GET.get('cassava')
    soquest = request.GET.get('soquest')
    coinmarketcap = request.GET.get('coinmarketcap')
    if carv == 'on':
        carv = 1
    if layer == 'on':
        layer = 2
    if ckg == 'on':
        ckg = 3
    if zeta == 'on':
        zeta = 4
    if cassava == 'on':
        cassava = 5
    if soquest == 'on':
        soquest = 6
    if coinmarketcap == 'on':
        coinmarketcap = 7
    # checkbox为复选框的值
    checkboxNum = [carv, layer, ckg, zeta, cassava, soquest, coinmarketcap]
    print(checkboxNum)
    inputNum = []
    for a in taskNum.split(','):
        inputNum.append(int(a))

    run_views.adsTask(inputNum, checkboxNum)

    return JsonResponse({'code': "任务执行完成"})


def bitTask(request):
    taskNum = request.GET.get('taskNum')
    carv = request.GET.get('carv')
    layer = request.GET.get('layer')
    ckg = request.GET.get('ckg')
    zeta = request.GET.get('zeta')
    cassava = request.GET.get('cassava')
    coinmarketcap = request.GET.get('coinmarketcap')
    if carv == 'on':
        carv = 1
    if layer == 'on':
        layer = 2
    if ckg == 'on':
        ckg = 3
    if zeta == 'on':
        zeta = 4
    if cassava == 'on':
        cassava = 5
    if coinmarketcap == 'on':
        coinmarketcap = 6
    # checkbox为复选框的值
    checkboxNum = [carv, layer, ckg, zeta, cassava, coinmarketcap]
    print(checkboxNum)
    inputNum = []
    for a in taskNum.split(','):
        inputNum.append(int(a))

    run_views.bitTask(inputNum, checkboxNum)

    return JsonResponse({'code': "任务执行完成"})


def adsAllTask(request):
    taskNum = request.GET.get('taskNum')
    inputNum = []
    for a in taskNum.split(','):
        inputNum.append(int(a))

    run_views.adsAllTask(inputNum)

    return JsonResponse({'code': "任务执行完成"})


def bitAllTask(request):
    taskNum = request.GET.get('taskNum')
    inputNum = []
    for a in taskNum.split(','):
        inputNum.append(int(a))

    run_views.bitAllTask(inputNum)

    return JsonResponse({'code': "任务执行完成"})


def runAdsFailTask(request):
    taskName = request.GET.get('taskName')
    num = request.GET.get('num')
    taskList = [int(num)]
    inputNum = []
    for a in taskName.split(','):
        inputNum.append(int(a))
    run_views.adsTask(inputNum, taskList)

    return JsonResponse({'code': "任务执行完成"})


def runFailTask(request):
    taskName = request.GET.get('taskName')
    num = request.GET.get('num')
    taskList = [int(num)]
    inputNum = []
    for a in taskName.split(','):
        inputNum.append(int(a))
    run_views.bitTask(inputNum, taskList)

    return JsonResponse({'code': "任务执行完成"})
