from django.db import models
from django.utils import timezone
import datetime
from dateutil.relativedelta import relativedelta

# レッスンのオブジェクト
class Lesson(models.Model):

  GENRE_CHOICES = (
    (1, '英語'),
    (2, 'ファイナンス'),
    (3, 'プログラミング'),
  )

  genre = models.IntegerField(verbose_name='ジャンル', choices=GENRE_CHOICES, blank=True, null=True)
  charge = models.CharField(max_length=200, verbose_name='基本料金')
  usage_fee = models.CharField(max_length=200, verbose_name='従量料金')

  def __int__(self):
    return self.genre

  def get_lesson_history(self):
    today = datetime.date.today()
    first_of_thismonth = today + relativedelta(day=1)
    nextmonth = today + relativedelta(months=1)
    end_of_thismonth = nextmonth + relativedelta(day=1)

    eng_m = []
    eng_w = []
    eng_m_unique_customer = []
    eng_w_unique_customer = []
    finance_m = []
    finance_w = []
    finance_m_unique_customer = []
    finance_w_unique_customer = []
    programing_m = []
    programing_w = []
    programing_m_unique_customer = []
    programing_w_unique_customer = []
    unique = []
    zenbu = []
    test = []
    zenbu = []
    price = []
    i = 0
    while i < 24:
      first_of_Nmonth_ago = first_of_thismonth - relativedelta(months=i)
      next_Nmonth = first_of_thismonth - relativedelta(months=(i-1))
      end_of_Nmonth_ago = next_Nmonth - relativedelta(days=1)
      lesson_per_month = Lesson_history.objects.filter(date__range=(first_of_Nmonth_ago, end_of_Nmonth_ago)) # 月毎の受講データを取得

      em_price = 0
      ew_price = 0
      fm_price = 0
      fw_price = 0
      pm_price = 0
      pw_price = 0

      for history in lesson_per_month:
        if history.lesson.genre == 1: # 英語の受講者
          if history.customer.gender == 1: # 英語を受講する男
            eng_m.append(history)
            eng_m_unique_customer.append(history.customer)
            fee = history.calculate_price()
            em_price += fee
          elif history.customer.gender == 2: # 英語を受講する女
            eng_w.append(history)
            eng_w_unique_customer.append(history.customer)
            fee = history.calculate_price()
            ew_price += fee

        elif history.lesson.genre == 2: # ファイナンスの受講者
          if history.customer.gender == 1: # ファイナンスを受講する男
            finance_m.append(history)
            finance_m_unique_customer.append(history.customer)
            fee = history.calculate_price()
            fm_price += fee
          elif history.customer.gender == 2: # ファイナンスを受講する女
            finance_w.append(history)
            finance_w_unique_customer.append(history.customer)
            fee = history.calculate_price()
            fw_price += fee

        elif history.lesson.genre == 3: # プログラミングを受講者
          if history.customer.gender == 1: # プログラミングを受講する男
            programing_m.append(history)
            programing_m_unique_customer.append(history.customer)
            fee = history.calculate_price()
            pm_price += fee
          elif history.customer.gender == 2: # プログラミングを受講する女
            programing_w.append(history)
            programing_w_unique_customer.append(history.customer)
            fee = history.calculate_price()
            pw_price += fee

      zenbu.append(((eng_m, eng_w), (finance_m, finance_w), (programing_m, programing_w)))
      price.append(((em_price, ew_price), (fm_price, fw_price), (pm_price, pw_price)))

      eng_m_unique_customer = list(set(eng_m_unique_customer))
      eng_w_unique_customer = list(set(eng_w_unique_customer))
      finance_m_unique_customer = list(set(finance_m_unique_customer))
      finance_w_unique_customer = list(set(finance_w_unique_customer))
      programing_m_unique_customer = list(set(programing_m_unique_customer))
      programing_w_unique_customer = list(set(programing_w_unique_customer))

      unique.append(((eng_m_unique_customer, eng_w_unique_customer), (finance_m_unique_customer, finance_w_unique_customer), (programing_m_unique_customer, programing_w_unique_customer)))

      test.append((first_of_Nmonth_ago, zenbu, unique, price))

      eng_m = []
      eng_w = []
      finance_m = []
      finance_w = []
      programing_m = []
      programing_w = []
      eng_m_unique_customer = []
      eng_w_unique_customer = []
      finance_m_unique_customer = []
      finance_w_unique_customer = []
      programing_m_unique_customer = []
      programing_w_unique_customer = []
      zenbu = []
      unique = []
      price = []

      i += 1
    return test


# 顧客のオブジェクト
class Customer(models.Model):

  GENDER_CHOICES = (
    (1, '男'),
    (2, '女'),
    (3, 'その他'),
  )
  name = models.CharField(max_length=255, verbose_name='名前')
  gender = models.IntegerField(verbose_name='性別', choices=GENDER_CHOICES, blank=True, null=True)
  age = models.CharField(max_length=200, verbose_name='年齢')

  def __str__(self):
    return self.name

  def getLessonHistory(self): # 受講履歴を取得
    today = datetime.date.today()
    first_of_thismonth = today + relativedelta(day=1)
    first_of_onemonth_ago = first_of_thismonth - relativedelta(months=1)
    first_of_twomonth_ago = first_of_thismonth - relativedelta(months=2)
    first_of_threemonth_ago = first_of_thismonth - relativedelta(months=3)
    nextmonth = today + relativedelta(months=1)
    end_of_thismonth = nextmonth + relativedelta(day=1)
    end_of_onemonth_ago = first_of_thismonth - relativedelta(days=1)
    end_of_twomonth_ago = first_of_onemonth_ago - relativedelta(days=1)
    end_of_threemonth_ago = first_of_twomonth_ago - relativedelta(days=1)

    thismonth_lesson = Lesson_history.objects.filter(customer=self.id, date__range=(first_of_thismonth, end_of_thismonth))
    onemonth_ago_lesson = Lesson_history.objects.filter(customer=self.id, date__range=(first_of_onemonth_ago, end_of_onemonth_ago))
    twomonth_ago_lesson = Lesson_history.objects.filter(customer=self.id, date__range=(first_of_twomonth_ago, end_of_twomonth_ago))
    threemonth_ago_lesson = Lesson_history.objects.filter(customer=self.id, date__range=(first_of_threemonth_ago, end_of_threemonth_ago))
    lesson_history = (thismonth_lesson, onemonth_ago_lesson, twomonth_ago_lesson, threemonth_ago_lesson)
    return lesson_history

  def getCountPerLesson(self): # 受講履歴カウント
    today = datetime.date.today()
    first_of_thismonth = today + relativedelta(day=1)
    first_of_onemonth_ago = first_of_thismonth - relativedelta(months=1)
    first_of_twomonth_ago = first_of_thismonth - relativedelta(months=2)
    first_of_threemonth_ago = first_of_thismonth - relativedelta(months=3)
    nextmonth = today + relativedelta(months=1)
    end_of_thismonth = nextmonth + relativedelta(day=1)
    end_of_onemonth_ago = first_of_thismonth - relativedelta(days=1)
    end_of_twomonth_ago = first_of_onemonth_ago - relativedelta(days=1)
    end_of_threemonth_ago = first_of_twomonth_ago - relativedelta(days=1)

    thismonth_history = Lesson_history.objects.filter(customer=self.id, date__range=(first_of_thismonth, end_of_thismonth))
    onemonth_ago_history = Lesson_history.objects.filter(customer=self.id, date__range=(first_of_onemonth_ago, end_of_onemonth_ago))
    twomonth_ago_history = Lesson_history.objects.filter(customer=self.id, date__range=(first_of_twomonth_ago, end_of_twomonth_ago))
    threemonth_ago_history = Lesson_history.objects.filter(customer=self.id, date__range=(first_of_threemonth_ago, end_of_threemonth_ago))
    history_per_month = [thismonth_history, onemonth_ago_history, twomonth_ago_history, threemonth_ago_history] # リストに各月毎のデータを格納

    countGenre_per_month = [] # 月毎にジャンルの受講回数をカウントして格納
    for histories in history_per_month:
      english = 0
      finance = 0
      programing = 0
      for history in histories:
        if history.lesson.genre == 1:
          english += 1
        elif history.lesson.genre == 2:
          finance += 1
        elif history.lesson.genre == 3:
          programing += 1

      genre_count = []
      if english >= 1:
        genre_count.append('英語(' + str(english) + ')')
      if finance >= 1:
        genre_count.append('ファイナンス(' + str(finance) + ')')
      if programing >= 1:
        genre_count.append('プログラム(' + str(programing) + ')')
      countGenre_per_month.append(genre_count)
    return countGenre_per_month

  def calculate_total_price(self): # 請求金額を計算
    today = datetime.date.today()
    first_of_thismonth = today + relativedelta(day=1)
    first_of_onemonth_ago = first_of_thismonth - relativedelta(months=1)
    first_of_twomonth_ago = first_of_thismonth - relativedelta(months=2)
    first_of_threemonth_ago = first_of_thismonth - relativedelta(months=3)
    nextmonth = today + relativedelta(months=1)
    first_of_nextmonth = nextmonth + relativedelta(day=1)
    end_of_thismonth = first_of_nextmonth - relativedelta(days=1)
    end_of_onemonth_ago = first_of_thismonth - relativedelta(days=1)
    end_of_twomonth_ago = first_of_onemonth_ago - relativedelta(days=1)
    end_of_threemonth_ago = first_of_twomonth_ago - relativedelta(days=1)

    thismonth_history = Lesson_history.objects.filter(customer=self.id, date__range=(first_of_thismonth, end_of_thismonth))
    onemonth_ago_history = Lesson_history.objects.filter(customer=self.id, date__range=(first_of_onemonth_ago, end_of_onemonth_ago))
    twomonth_ago_history = Lesson_history.objects.filter(customer=self.id, date__range=(first_of_twomonth_ago, end_of_twomonth_ago))
    threemonth_ago_history = Lesson_history.objects.filter(customer=self.id, date__range=(first_of_threemonth_ago, end_of_threemonth_ago))
    history_per_month = [thismonth_history, onemonth_ago_history, twomonth_ago_history, threemonth_ago_history] # リストに各月毎のデータを格納

    total_price_per_month = [] # 月毎の請求金額を格納する空リスト
    for histories in history_per_month:
      total_price = 0
      for history in histories:
        price_per_lesson = 0
        hour = int(history.hour)
        charge = int(history.lesson.charge)
        usage_fee = int(history.lesson.usage_fee)

        # ---------------英語の価格計算--------------------
        if history.lesson.genre == 1:
          price_per_lesson = charge + (usage_fee * hour)

        # ------------ファイナンスの価格計算----------------
        elif history.lesson.genre == 2:
          volume_discount = 2800
          volume_discount_two = 2500

          if hour > 20 and 50 >= hour: #20万円を超え、50万円以下の時
            price_per_lesson = charge + (usage_fee * 20) + (volume_discount * (hour - 20))
          elif hour > 50: #50万円を超える時
            price_per_lesson = charge + (usage_fee * 20) + (volume_discount * 30) + (volume_discount_two * (hour - 50))
          else:
            price_per_lesson = charge + (usage_fee * hour)

        # ------------プログラミングの価格計算--------------
        elif history.lesson.genre == 3:
          volume_discount = 3000
          volume_discount_two = 2800
          volume_discount_three = 2500
          if hour <= 5: #5万円以下の時
            price_per_lesson = charge
          elif hour > 5 and 20 >= hour: #5万円を超え、20万円以下の時
            price_per_lesson = charge + (usage_fee * (hour - 5))
          elif hour > 20 and 35 >= hour: #20万円を超え、35万円以下の時
            price_per_lesson = charge + (usage_fee * 15) + (volume_discount * (hour - 20))
          elif hour > 35 and 50 >= hour: #35万円を超え、50万円以下の時
            price_per_lesson = charge + (usage_fee * 15) + (volume_discount * 15) + (volume_discount_two * (hour - 35))
          elif hour > 50: #50万円を超える時
            price_per_lesson = charge + (usage_fee * 15) + (volume_discount * 15) + (volume_discount_two * 15) + (volume_discount_three * (hour - 50))
        total_price += price_per_lesson
      total_price_per_month.append(total_price)
    return total_price_per_month

# 受講記録のオブジェクト
class Lesson_history(models.Model):
  customer = models.ForeignKey(Customer, verbose_name="顧客名")
  lesson = models.ForeignKey(Lesson, verbose_name="ジャンル")
  date = models.DateField(default=timezone.now, verbose_name="受講日")
  hour = models.CharField(max_length=200, verbose_name='受講時間(h)')

  def __int__(self):
    return self.date

  def calculate_price(self):
    hour = int(self.hour)
    charge = int(self.lesson.charge)
    usage_fee = int(self.lesson.usage_fee)

    if self.lesson.genre == 2: #ファイナンスの価格計算
      volume_discount = 2800
      volume_discount_two = 2500
      if hour > 20 and 50 >= hour:
        return charge + (usage_fee * 20) + (volume_discount * (hour - 20))
      elif hour > 50:
        return charge + (usage_fee * 20) + (volume_discount * 30) + (volume_discount_two * (hour - 50))

    elif self.lesson.genre == 3: #プログラミングの価格計算
      volume_discount = 3000
      volume_discount_two = 2800
      volume_discount_three = 2500
      if hour <= 5:
        return charge
      elif hour > 5 and 20 >= hour:
        return charge + (usage_fee * (hour - 5))
      elif hour > 20 and 35 >= hour:
        return charge + (usage_fee * 15) + (volume_discount * (hour - 20))
      elif hour > 35 and 50 >= hour:
        return charge + (usage_fee * 15) + (volume_discount * 15) + (volume_discount_two * (hour - 35))
      elif hour > 50:
        return charge + (usage_fee * 15) + (volume_discount * 15) + (volume_discount_two * 15) + (volume_discount_three * (hour - 50))
    return charge + (usage_fee * hour)
