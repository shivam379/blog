from django.shortcuts import render
from .models import BlogPost


def dashboard(request):
    status = True
    blogs = []
    current_page = int(request.GET.get("page", "1"))
    limit = 2
    previous_page = 1
    next_page = 1
    total_pages = 1
    skip = 0
    try:
        if current_page> 1:
            skip = (current_page - 1) * limit
        blogs = BlogPost.objects.all().order_by("-pub_date")[skip: skip+limit]
        blog_count = BlogPost.objects.count()
        if blog_count:
            total_pages = int(blog_count / limit)
            if (blog_count) % limit:
                total_pages += 1
            previous_page = max(current_page - 1, 1)
            next_page = min(current_page + 1, total_pages)
    except:
        status = False
    finally:
        response = {"data": blogs,
                    "status": status,
                    "previous_page": previous_page,
                    "next_page": next_page,
                    "total_pages": total_pages,
                    "current_page": current_page
                    }

        return render(request, 'list.html', response)
