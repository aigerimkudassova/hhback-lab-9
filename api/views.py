from django.shortcuts import render
from django.http.response import JsonResponse
from api.models import Company, Vacancy
from django.db.models import Count


def company_list(request):
    companies = Company.objects.all()
    companies_json = [company.company_to_json() for company in companies]
    return JsonResponse(companies_json, safe=False)


def company_detail(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    return JsonResponse(company.company_to_json())


def vacancies_list(request):
    if request.method == "GET":
        vacancies = Vacancy.objects.all()
        vacancies_json = [vacancy.vacancy_to_json() for vacancy in vacancies]
        return JsonResponse(vacancies_json, safe=False)


def vacancy_detail(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'errorL': 'vacancy doesn`t exist'})
    return JsonResponse(vacancy.vacancy_to_json())


def company_vacancies(request, company_id):
    if request.method == "GET":
        try:
            company = Company.objects.get(id=company_id)
        except Company.DoesNotExist as e:
            return JsonResponse({'error': str(e)})

        vacancies = company.vacancy_set.all()
        vacancies_json = [v.vacancy_to_json() for v in vacancies]
        return JsonResponse(vacancies_json, safe=False)


def top_vacancies(request):
    if request.method == "GET":
        vacancies = Vacancy.objects.annotate(Count('salary')).order_by('-salary')[:10]
        vacancies_json = [vacancy.vacancy_to_json() for vacancy in vacancies]
        return JsonResponse(vacancies_json, safe=False)
