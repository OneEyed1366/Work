cd C:\Users\proka\virtuals\python\django\rossoshrealty\familyan
echo "Update DB -> ..." && python manage.py update_base
echo "Update our team -> ..." && python manage.py update_ourTeam
echo "Update our services -> ..." && python manage.py update_services
echo "Update news -> ..." && python manage.py update_news
echo "Update properties -> ..." && python manage.py update_properties
echo "Update properties carousel -> ..." && python manage.py update_propertiesCarousel
echo "Update properties similars -> ..." && python manage.py update_propertiesSimilars
echo "DB -> Updated!" && git add -A && git comm "update" && git push