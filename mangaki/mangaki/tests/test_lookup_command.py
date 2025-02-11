# SPDX-FileCopyrightText: 2014, Mangaki Authors
# SPDX-License-Identifier: AGPL-3.0-only

from django.core.management import call_command
from django.test import TestCase
from django.utils.six import StringIO

from mangaki.models import Work, Category, Editor, Studio

class LookupTest(TestCase):
    def setUp(self):
        anime = Category.objects.get(slug='anime')
        Work.objects.create(
            title='Steins;Gate',
            source='Ryan',
            category=anime
        )

    def test_lookup_steins_gate(self):
        out = StringIO()

        call_command('lookup', 'Steins;Gate', stdout=out)
        output = out.getvalue().lower()

        self.assertIn('steins;gate', output)
        self.assertIn('counter', output)
