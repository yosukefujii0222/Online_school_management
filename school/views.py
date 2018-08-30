from django.shortcuts import render
from .models import Lesson, Customer, Lesson_history
from .forms import CustomerForm
from django.shortcuts import get_object_or_404
from .forms import LessonHistoryForm
import datetime
from dateutil.relativedelta import relativedelta


def lesson_list(request):
  lessons = Lesson.objects.all()
  return render(request, 'school/lesson_list.html', {'lessons': lessons})

def customer_list(request):
  customers = Customer.objects.all()
  return render(request, 'school/customer_list.html', {'customers': customers})

def lesson_history(request):
  histories = Lesson_history.objects.all()
  return render(request, 'school/lesson_history.html', {'histories': histories})

def monthly_report(request):
  month = request.GET.get('month')
  customers = Customer.objects.all()
  today = datetime.date.today() #今日
  first_of_thismonth = today + relativedelta(day=1)
  first_of_onemonth_ago = first_of_thismonth - relativedelta(months=1)
  first_of_twomonth_ago = first_of_thismonth - relativedelta(months=2)
  first_of_threemonth_ago = first_of_thismonth - relativedelta(months=3)

  return render(request, 'school/monthly_report.html', {'customers': customers, 'first_of_thismonth': first_of_thismonth, 'first_of_onemonth_ago': first_of_onemonth_ago, 'first_of_twomonth_ago': first_of_twomonth_ago, 'first_of_threemonth_ago': first_of_threemonth_ago, 'month': month})


def report(request):
  dateSelect = request.GET.get('dateSelect')
  lessons = Lesson.objects.all()
  histories = Lesson_history.objects.all()
  ages = [(0, 10), (1, 20), (2, 30), (3, 40), (4, 50), (5, 60), (6, 70)]
  alldata = Lesson_history.objects.all()

  # --過去2年のリスト--
  today = datetime.date.today()
  first_of_thismonth = today + relativedelta(day=1)
  count = 1
  index =  range(24)
  date_list = [first_of_thismonth] # 過去2年間を格納するリスト
  while count <= 24:
    month = first_of_thismonth - relativedelta(months=count)
    date_list.append(month)
    count += 1
  # --ここまで--

  # -----------------ジャンルと性別別にソート------------------------

  # 顧客ごとのレッスン時間、レッスン数の配列を宣言
  genre_gender = []
  # 元データをループ
  i = 0
  for item in alldata:
    firstOfMonth = item.date + relativedelta(day=1) # 受講日の月初を計算

    # ある顧客のデータを保持する配列
    stat = {}
    for d in genre_gender:
      if d['month'] == firstOfMonth and d['genre'] == item.lesson.genre and d['gender'] == item.customer.gender:
        stat = d
    i += 1
    # statが空の時には、初期値を詰め込む
    if len(stat) == 0:
      stat = {
        'month': firstOfMonth,
        'genre': item.lesson.genre,
        'gender': item.customer.gender,
        'age': round(int(item.customer.age) / 10) * 10,
        'lessonHours': 0,
        'lessonCount': 0,
        'amount': 0,
        'person': [item.customer.id]
      }
      genre_gender.append(stat)
    stat['lessonHours'] += int(item.hour)
    stat['lessonCount'] += 1
    # 受講者がユニークであれば保存
    if item.customer.id in stat['person']:
      pass
    else:
      stat['person'].append(item.customer.id)

  for customer in genre_gender:
    # 英語の価格計算
    if customer['genre'] == 1:
      customer['amount'] = 5000 + (3500 * customer['lessonHours'])

    # ファイナンスの価格計算
    elif customer['genre'] == 2:

      if customer['lessonHours'] > 20 and 50 >= customer['lessonHours']: #20万円を超え、50万円以下の時
        customer['amount'] = (3300 * 20) + (2800 * (customer['lessonHours'] - 20))
      elif customer['lessonHours'] > 50: #50万円を超える時
        customer['amount'] = (3300 * 20) + (2800 * 30) + (2500 * (customer['lessonHours'] - 50))
      else:
        customer['amount'] = 3300 * customer['lessonHours']

    # プログラミングの価格計算
    elif customer['genre'] == 3:
      if customer['lessonHours'] <= 5: #5万円以下の時
        customer['amount'] = 20000
      elif customer['lessonHours'] > 5 and 20 >= customer['lessonHours']: #5万円を超え、20万円以下の時
        customer['amount'] = 20000 + (3500 * (customer['lessonHours'] - 5))
      elif customer['lessonHours'] > 20 and 35 >= customer['lessonHours']: #20万円を超え、35万円以下の時
        customer['amount'] = 20000 + (3500 * 15) + (3000 * (customer['lessonHours'] - 20))
      elif customer['lessonHours'] > 35 and 50 >= customer['lessonHours']: #35万円を超え、50万円以下の時
        customer['amount'] = 20000 + (3500 * 15) + (3000 * 15) + (2800 * (customer['lessonHours'] - 35))
      elif customer['lessonHours'] > 50: #50万円を超える時
        customer['amount'] = 20000 + (3500 * 15) + (3000 * 15) + (2800 * 15) + (2500 * (customer['lessonHours'] - 50))
 # -------------------------------------------------------------------

  # -----------------ジャンルと年齢層別にソート------------------------

  # 顧客ごとのレッスン時間、レッスン数の配列を宣言
  customerLessons = []
  # 元データをループ
  i = 0
  for item in alldata:
    firstOfMonth = item.date + relativedelta(day=1) # 受講日の月初を計算

    # ある顧客のデータを保持する配列
    stat = {}
    for d in customerLessons:
      if d['month'] == firstOfMonth and d['genre'] == item.lesson.genre and d['gender'] == item.customer.gender and d['age'] == round(int(item.customer.age) / 10) * 10:
        stat = d
    i += 1
    # statが空の時には、初期値を詰め込む
    if len(stat) == 0:
      stat = {
        'month': firstOfMonth,
        'genre': item.lesson.genre,
        'gender': item.customer.gender,
        'age': round(int(item.customer.age) / 10) * 10,
        'lessonHours': 0,
        'lessonCount': 0,
        'amount': 0,
        'person': [item.customer.id]
      }
      customerLessons.append(stat)
    stat['lessonHours'] += int(item.hour)
    stat['lessonCount'] += 1
    # 受講者がユニークであれば保存
    if item.customer.id in stat['person']:
      pass
    else:
      stat['person'].append(item.customer.id)

  for customer in customerLessons:
    # 英語の価格計算
    if customer['genre'] == 1:
      customer['amount'] = 5000 + (3500 * customer['lessonHours'])

    # ファイナンスの価格計算
    elif customer['genre'] == 2:

      if customer['lessonHours'] > 20 and 50 >= customer['lessonHours']: #20万円を超え、50万円以下の時
        customer['amount'] = (3300 * 20) + (2800 * (customer['lessonHours'] - 20))
      elif customer['lessonHours'] > 50: #50万円を超える時
        customer['amount'] = (3300 * 20) + (2800 * 30) + (2500 * (customer['lessonHours'] - 50))
      else:
        customer['amount'] = 3300 * customer['lessonHours']

    # プログラミングの価格計算
    elif customer['genre'] == 3:
      if customer['lessonHours'] <= 5: #5万円以下の時
        customer['amount'] = 20000
      elif customer['lessonHours'] > 5 and 20 >= customer['lessonHours']: #5万円を超え、20万円以下の時
        customer['amount'] = 20000 + (3500 * (customer['lessonHours'] - 5))
      elif customer['lessonHours'] > 20 and 35 >= customer['lessonHours']: #20万円を超え、35万円以下の時
        customer['amount'] = 20000 + (3500 * 15) + (3000 * (customer['lessonHours'] - 20))
      elif customer['lessonHours'] > 35 and 50 >= customer['lessonHours']: #35万円を超え、50万円以下の時
        customer['amount'] = 20000 + (3500 * 15) + (3000 * 15) + (2800 * (customer['lessonHours'] - 35))
      elif customer['lessonHours'] > 50: #50万円を超える時
        customer['amount'] = 20000 + (3500 * 15) + (3000 * 15) + (2800 * 15) + (2500 * (customer['lessonHours'] - 50))
 # -------------------------------------------------------------------

  return render(request, 'school/report.html', {'dateSelect': dateSelect, 'lessons': lessons, 'ages': ages, 'date_list': date_list, 'histories': histories, 'customerLessons': customerLessons, 'genre_gender': genre_gender})

def new_customer(request):
  if request.method == "POST":
    form = CustomerForm(request.POST)
    if form.is_valid():
      new = form.save(commit=False)
      new.save()
      form = CustomerForm()
      return render(request, 'school/new_customer.html', {'form': form})
  else:
    form = CustomerForm()
    return render(request, 'school/new_customer.html', {'form': form})

def customer_edit(request, pk):
  customer = get_object_or_404(Customer, pk=pk)
  if request.method == "POST":
    form = CustomerForm(request.POST, instance=customer)
    if form.is_valid():
      new = form.save(commit=False)
      new.save()
      customers = Customer.objects.all()
      return render(request, 'school/customer_list.html', {'customers': customers})
  else:
    form = CustomerForm(instance=customer)
    return render(request, 'school/customer_edit.html', {'form': form})

def new_lesson_history(request):
  if request.method == "POST":
    form = LessonHistoryForm(request.POST)
    if form.is_valid():
      new = form.save(commit=False)
      new.save()
      form = LessonHistoryForm()
      return render(request, 'school/new_lesson_history.html', {'form': form})
  else:
    form = LessonHistoryForm()
    return render(request, 'school/new_lesson_history.html', {'form': form})

def lesson_history_edit(request, pk):
  lesson_history = get_object_or_404(Lesson_history, pk=pk)
  if request.method == "POST":
    form = LessonHistoryForm(request.POST, instance=lesson_history)
    if form.is_valid():
      new = form.save(commit=False)
      new.save()
      histories = Lesson_history.objects.all()
      return render(request, 'school/lesson_history.html', {'histories': histories})
  else:
    form = LessonHistoryForm(instance=lesson_history)
    return render(request, 'school/lesson_history_edit.html', {'form': form})
