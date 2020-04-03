from django.contrib import admin
from django.urls import path

from api.views import company_list, company_detail, vacancies_list, vacancy_detail, top_vacancies, company_vacancies

urlpatterns = [
    path('companies/', company_list),
    path('companies/<int:company_id>/', company_detail),
    path('vacancies/', vacancies_list),
    path('vacancies/<int:vacancy_id>/', vacancy_detail),
    path('companies/<int:company_id>/vacancies', company_vacancies),
    path('vacancies/top_ten', top_vacancies)
]