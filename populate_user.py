import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'first_project.settings')

import django
django.setup()

from first_app.models import Projects
from faker import Faker

fakgen = Faker()

def populate(N = 5):
    for entry in range(N):
        fake_title = fakgen.bs()
        fake_technologies = fakgen.windows_platform_token()
        fake_detail = fakgen.sentences(nb=3, ext_word_list=None)
        fake_url = fakgen.url()
        fake_git = fakgen.sentences(nb=1, ext_word_list=None)

        #entries
        user = Projects.objects.get_or_create(title = fake_title, technologies = fake_technologies, detail = fake_detail,
                                            url_project = fake_url, github_link = fake_git)[0]
if __name__ == '__main__':
    print("populating start")
    populate(20)
    print('finished')
