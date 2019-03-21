import sys

from report import Report
import cli


try:
    tid = sys.argv[1]
except IndexError:
    tid = "241584"
report = Report(tid)
title = report.title


def total_count(rep):
    cli.printC("Total Signatures: {}".format(rep.get_count()), cli.HEADER)


def search_country(rep):
    query = cli.question("Enter your search term").strip()
    matches = rep.search_country(query)
    rep.print_countries(matches)


def search_mp(rep):
    query = cli.question("Enter your search term").strip()
    matches = rep.search_mp(query)
    rep.print_mps(matches)


def list_country(rep):
    rep.print_countries(rep.countries)


def list_mp(rep):
    rep.print_mps(rep.mps)


defs = [total_count, search_country, search_mp, list_country, list_mp]

options = [
    "{:30}| Total count of all Signatures".format("Signatures"),
    "{:30}| Search for country containing a term".format("Search Country"),
    "{:30}| Search for how many people in an MP's constituency signed".format("Search by MP"),
    "{:30}| Table Of all signatures by country".format("List Countries"),
    "{:30}| Table Of all signatures by constituency".format("List Constituency"),
]
cli.build_cli(title, options, defs, rep=report)