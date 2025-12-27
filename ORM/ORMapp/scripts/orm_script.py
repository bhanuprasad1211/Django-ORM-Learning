from ORMapp.models import Restaurent,Rating,Sales,Staff,Product,Comments
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.functions import Upper,Lower,Length,Concat,Coalesce
from django.db import connection,transaction
from django.db.models import Count,Avg,Max,Min,Sum,Value,CharField,F,Q,Case,When
from pprint import pprint
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.admin import GenericTabularInline

import time
import random,itertools
#run these commands before executing script
# env) bha:~/DjangoORM/ORM$ sudo systemctl stop postgresql
# [sudo] password for bhanuprasad: 
# (env) bha:~/DjangoORM/ORM$ sudo docker start pg_container
def run() :
    restaurents=Restaurent.objects.first()
    print(restaurents.ratings.first())
    # restaurent=Restaurent.objects.first()
    # comment=Comments.objects.create(
    #     text='It is good',
    #     content_object=restaurent,
    # )
    # print(comment)
    # print(comment.__dict__)
    # comment=Comments.objects.first()
    # ctype=comment.content_type
    # model=ctype.get_all_objects_for_this_type(id=comment.object_id)
    # print(model)
    # print(type(model))
    # comments=Comments.objects.all()
    # for comment in comments :
    #     print(comment.content_object)
    # models=ContentType.objects.filter(app_label='ORMapp')
    # print([c.model for c in models])
    # content_type=ContentType.objects.get(app_label='ORMapp',model='restaurent')
    # restaurent_type=content_type.model_class()
    # restaurent_model=content_type.get_all_objects_for_this_type(name='McDonalds').first()
    # print(restaurent_model.latitude)
    #print(restaurent_model.latitude)
    #id app_label model 

    # with transaction.atomic() :
    #     book=Product.objects.select_for_update().get(name='Book')
    #     time.sleep(60)

    # restuarents=Restaurent.objects.filter(sales__income__gt=85).values('name','sales__income')
    # print(restuarents.count())

    # restuarents=Restaurent.objects.annotate(total_income=Sum('sales__income')).filter(total_income__gt=85)
    # print(restuarents.values('name','total_income'))
    # first_sale=Sales.objects.aggregate(first_sale=Min('datetime'))['first_sale']
    # last_sale=Sales.objects.aggregate(last_sale=Max('datetime'))['last_sale']
    # dates=[]
    # count=itertools.count()
    # while (dt:=first_sale + timezone.timedelta(days=10*next(count)))<=last_sale :
    #     dates.append(dt)
    # whens=[
    #     When(datetime__range=(dt,dt+timezone.timedelta(days=10)),then=Value(dt.date())) for dt in dates
    # ]
    # case=Case(
    #     *whens,output_field=CharField()
    # )
    # print(
    #     Sales.objects.annotate(
    #         daterange=case
    #     ).values('daterange').annotate(total_sales=Sum('income'))
    # )
    # restaurents=Restaurent.objects.annotate(avg_rating=Avg('ratings__rating'),rating_count=Count('ratings__rating'))
    # restaurents=restaurents.annotate(
    #     rating_bucket=Case(
    #         When(avg_rating__gt=3.5,then=Value('High rating')),
    #         When(avg_rating__range=(2.5,3.5),then=Value('Average rating')),
    #         When(avg_rating__lt=2.5,then=Value('Bad rating')),
    #     )
    # )
    # print(restaurents.filter(rating_bucket='High rating').values('name'))
    # restaurents=Restaurent.objects.annotate(avg_rating=Avg('ratings__rating')).filter(avg_rating__gt=3.5)
    # restaurents=Restaurent.objects.annotate(rating_count=Count('ratings__rating')).filter(rating_count__gt=1)

    # italian=Restaurent.TypeChoice.ITALIAN
    # restaurents=Restaurent.objects.annotate(
    #     is_italian=Case(
    #         When(restaurent_type=italian,then=True),
    #         default=False
    #     )
    # )
    #print(restaurents.filter(is_italian=True))

    # print(
    #     Restaurent.objects.annotate(name_value=Coalesce(F('nickname'),F('name'))).values('name_value')
    # )

    # print(Restaurent.objects.aggregate(summ=Coalesce(Sum('capacity'),0)))
    # print(Rating.objects.filter(rating__lt=0).aggregate(avg=Coalesce(Avg('rating'),0.0)))
    # print(Rating.objects.filter(rating__lt=0).aggregate(avg=Avg('rating',default=0.0))) better to use default instead of Coalesce
    #Restaurent.objects.update(capacity=None)

    #print(Restaurent.objects.filter(capacity__isnull=False).order_by('capacity').values('capacity').reverse())


    # pro_gt_exp=Q(income__gt=F('expenditure'))
    # name_has_num=Q(restaurent__name__regex=r"[0-9]+")
    # sales=Sales.objects.filter(pro_gt_exp | name_has_num)
    # print(sales)

    # it_ot_mx=Q(name__icontains='italian') | Q(name__icontains='mexican')
    # recently_opened=Q(date_opened__gt=timezone.now() - timezone.timedelta(days=40))

    # restaurents=Restaurent.objects.filter(it_ot_mx | recently_opened).values('name','date_opened')
    # print(restaurents)

    #get all italian or mexican restaurents
    # IT=Restaurent.TypeChoice.ITALIAN
    # MX=Restaurent.TypeChoice.MEXICAN
    # restaurents=Restaurent.objects.filter(Q(restaurent_type=IT) | Q(restaurent_type=MX))
    # print(restaurents)
    # print(Restaurent.objects.filter(name__icontains='1'))
    # print(Restaurent.objects.filter(name__endswith='1'))
    # print(Restaurent.objects.filter(name__startswith='1'))
    # pprint(connection.queries)
    # sales=Sales.objects.aggregate(
    #     profit=Count('id',filter=Q(income__gt=F('expenditure')))
    # )
    # print(sales)

    # sales=Sales.objects.annotate(
    #     profit=F('income')-F('expenditure')
    # )
    # print(sales.first().profit)

    # sales=Sales.objects.filter(expenditure__gt=F('income')).values('expenditure','income')
    # pprint(sales)
    # sales=Sales.objects.all()
    # for sale in sales :
    #     sale.expenditure=random.uniform(5,100)
    #     #sale.save() use bulk update
    # Sales.objects.bulk_update(sales,['expenditure'])

    # ratings=Rating.objects.filter(rating=4).first()
    # ratings.rating=F('rating')-1
    # print(connection.queries)

    # restaurents=Restaurent.objects.annotate(total_sales=Sum('sales__income')).order_by('total_sales')#use - for reverse order
    # for r in restaurents :
    #     print(r.total_sales)
    

    # restaurents=Restaurent.objects.annotate(ratings_count=Count('ratings__rating'))
    # print(restaurents.values('name','ratings_count'))

    # restautents=Restaurent.objects.annotate(total_sales=Sum('sales__income'))
    # print([r.total_sales for r in restautents])

    # concatenation=Concat(
    #     'name',Value('[Rating ]'),Avg('ratings__rating'),Value(' ]'),output_field=CharField()
    # )
    # restaurents=Restaurent.objects.annotate(message=concatenation)
    # for r in restaurents :
    #     print(r.message)

    # restaurents=Restaurent.objects.annotate(len_name=Length('name')).filter(len_name__gte=10)
    # print(restaurents.values('name','len_name'))

    # one_month_ago=timezone.now() - timezone.timedelta(days=31)
    # sales=Sales.objects.filter(datetime__gte=one_month_ago)
    # print(
    #     sales.aggregate(sum=Sum('income'),min=Min('income'))
    # )

    # IN=Restaurent.TypeChoice.INDIAN
    # print(Rating.objects.filter(restaurent__restaurent_type=IN).aggregate(min=Min('rating'),max=Max('rating')))
    # print(connection.queries)

    # print(Restaurent.objects.aggregate(avg=Avg('ratings__rating')))
    # print(Rating.objects.filter(restaurent__name__startswith='c').aggregate(avg=Avg('rating')))
    # print(Restaurent.objects.aggregate(total=Count('id')))

    # restaurents=Restaurent.objects.values_list('name',flat=True) #flat returns a list 
    # print(restaurents)
    # IT=Restaurent.TypeChoice.ITALIAN
    # ratings=Rating.objects.filter(restaurent__restaurent_type=IT).values('rating','restaurent__name')
    # print(ratings)
    # restaurents=Restaurent.objects.values(name_upper=Upper('name'))[:3]#Database level operation
    # print(restaurents)

    # restaurents=Restaurent.objects.values('name','date_opened')
    # print(restaurents)

    # restaurent=Restaurent.objects.get(pk=22)
    # print(restaurent.staff_set.all())

    # staff,created=Staff.objects.get_or_create(
    #     name="John Wick"
    # )
    # staff.restaurents.set(Restaurent.objects.all()[:10])
    # print(staff.restaurents.count())
    #add,all,count,set,clear,remove
    #staff.restaurents.add(Restaurent.objects.first())
    # restaurents=Restaurent.objects.filter(name__startswith='C')
    # print(restaurents.ratings.all())

    # restaurents=Restaurent.objects.earliest() no need to mention date if we use Meta class with get_latest_by
    # print(restaurents)
    # restaurents=Restaurent.objects.all()
    #restaurents=Restaurent.objects.earliest('date_opened')
    #restaurents=Restaurent.objects.latest('date_opened')
    # print(restaurents)
    # print(connection.queries)
    # sales=Sales.objects.filter(income__range=(50,60))
    # print([sale.income for sale in sales])
    # print(sales)
    # print(connection.queries)

    # chines=Restaurent.TypeChoice.CHINES
    # indians=Restaurent.TypeChoice.INDIAN
    # restaurents=Restaurent.objects.filter(restaurent_type__in=[chines,indians])
    # restaurents=Restaurent.objects.exclude(restaurent_type__in=[chines,indians])
    # print(restaurents)
    # print(connection.queries)

    # restaurent=Restaurent.objects.filter(restaurent_type=Restaurent.TypeChoice.INDIAN)
    # print(restaurent)
    # print(restaurent.exists())
    # print(connection.queries)

    # Restaurent.objects.filter(name__exact='Pizza Shop').delete()

    # print(Rating.objects.get_or_create(
    #     user=User.objects.first(),
    #     restaurent=Restaurent.objects.all()[1],
    #     rating=3
    # ))
    # print(connection.queries)
    # restuarent=Restaurent.objects.first()
    # restuarent.delete()
    # restuarent=Restaurent.objects.filter(name__startswith='I')
    # print(restuarent)
    # print(restuarent.update(
    #     date_opened=timezone.now(),
    #     website='https://docs.djangoproject.com'
    # ))
    # print(connection.queries)

    #for updating all fields
    # restaurent=Restaurent.objects.all()
    # restaurent.update(
    #     date_opened=timezone.now()
    # )
    # print(connection.queries)

    #for updating
    # restaurent=Restaurent.objects.first()
    # print(restaurent)
    # restaurent.name="It is new Name"
    # restaurent.save(update_fields=['name']) #If we don't mention, it will update all fields 
    # print(connection.queries)

    # restaurent=Restaurent.objects.first()
    # user=User.objects.first()
    # rating=Rating.objects.create(
    #     user=user,
    #     restaurent=restaurent,
    #     rating=10
    # )
    # rating.full_clean() #It will validate fields before saving 
    # rating.save()
    # restaurent=Restaurent.objects.first()
    # user=User.objects.first()
    # print(Rating.objects.get_or_create(
    #     user=user,
    #     restaurent=restaurent,
    #     rating=2
    # ))
    #pprint(connection.queries)
    # restaurent=Restaurent.objects.first()
    # print(restaurent.sales.all())

    # Sales.objects.create(
    #     restaurent=Restaurent.objects.first(),
    #     datetime=timezone.now(),
    #     income=55.5,

    # )
    # Sales.objects.create(
    #     restaurent=Restaurent.objects.first(),
    #     datetime=timezone.now(),
    #     income=65.5,

    # )
    # Sales.objects.create(
    #     restaurent=Restaurent.objects.first(),
    #     datetime=timezone.now(),
    #     income=100.99,

    
    # restaurent=Restaurent.objects.first()
    # print(restaurent.ratings.all()) after modification of related name

    #backward quering
    # restaurent=Restaurent.objects.first()
    # print(restaurent.rating_set.all()[0])

    # rating=Rating.objects.first()
    # print(rating)
    # print(rating.restaurent)


    # restaurent=Restaurent.objects.first()
    # print(restaurent)
    # restaurent.name="Banny Italian"
    # restaurent.save()
    # print(restaurent)

    # print(Rating.objects.filter(rating=3))
    # print(Rating.objects.filter(rating=5))
    # Rating.objects.filter(rating__gte=4)

    # restaurent=Restaurent.objects.first()
    # user=User.objects.first()
    # rating=Rating.objects.create(user=user,restaurent=restaurent,rating=3)

    # print(Restaurent.objects.count())
    # print(connection.queries)

    #CREATING row using create 
    # Restaurent.objects.create(
    #     name='Pizza Shop',
    #     date_opened=timezone.now(),
    #     latitude=50.5,
    #     longitude=50.5,
    #     restaurent_type=Restaurent.TypeChoice.CHINES

    # )

    #python3 manage.py shell_plus --print-sql to run queries in InteractiveConsole

    # restaurent=Restaurent.objects.all() all object in db
    #restaurent=Restaurent.objects.first() first one only
    #restaurent=Restaurent.objects.all()[0] indexing
    # print(restaurent)
    # print(connection.queries)


    #To insert data into databases
    # restaurent=Restaurent()
    # restaurent.name="My Italian Restaurent"
    # restaurent.latitude=50.2
    # restaurent.longitude=50.2
    # restaurent.date_opened=timezone.now()
    # restaurent.restaurent_type=Restaurent.TypeChoice.ITALIAN
    # restaurent.save()