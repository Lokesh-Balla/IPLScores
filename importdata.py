import click
import openpyxl
import ipl
import iplpage
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'iplpage.settings')
django.setup()

@click.group()
def main():
    pass

@click.command()
@click.argument('filename',nargs=1)
def ImportMatches(filename):
    



if __name__=='__main__':
    main()