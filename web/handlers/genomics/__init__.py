from .lineage import LineageByCountryHandler, LineageByDivisionHandler, LineageAndCountryHandler, LineageAndDivisionHandler, LineageHandler, LineageMutationsHandler, MutationDetailsHandler, MutationsByLineage
from .prevalence import GlobalPrevalenceByTimeHandler, PrevalenceByCountryAndTimeHandler, PrevalenceByDivisionAndTimeHandler, PrevalenceByCountyAndTimeHandler, CumulativeGlobalPrevalenceHandler, CumulativePrevalenceByCountryHandler, CumulativePrevalenceByDivisionHandler, PrevalenceAllLineagesByCountryHandler, PrevalenceAllLineagesByDivisionHandler, PrevalenceAllLineagesByCountyHandler, PrevalenceByAAPositionHandler
from .general import LocationHandler, MetadataHandler, MutationHandler, SubmissionLagHandler, SequenceCountHandler, MostRecentCollectionDateGlobalHandler, MostRecentCollectionDateByCountryHandler, MostRecentCollectionDateByDivisionHandler, MostRecentCollectionDateByCountyHandler, MostRecentSubmissionDateGlobalHandler, MostRecentSubmissionDateByCountryHandler, MostRecentSubmissionDateByDivisionHandler, MostRecentSubmissionDateByCountyHandler

routes = [
    (r"/genomics/lineage-by-country", LineageByCountryHandler),
    (r"/genomics/lineage-by-division", LineageByDivisionHandler),
    (r"/genomics/lineage-and-country", LineageAndCountryHandler),
    (r"/genomics/lineage-and-division", LineageAndDivisionHandler),
    (r"/genomics/sequence-count", SequenceCountHandler),
    (r"/genomics/global-prevalence", GlobalPrevalenceByTimeHandler),
    (r"/genomics/prevalence-by-country", PrevalenceByCountryAndTimeHandler),
    (r"/genomics/prevalence-by-division", PrevalenceByDivisionAndTimeHandler),
    (r"/genomics/prevalence-by-county", PrevalenceByCountyAndTimeHandler),
    (r"/genomics/prevalence-by-country-all-lineages", PrevalenceAllLineagesByCountryHandler),
    (r"/genomics/prevalence-by-division-all-lineages", PrevalenceAllLineagesByDivisionHandler),
    (r"/genomics/prevalence-by-county-all-lineages", PrevalenceAllLineagesByCountyHandler),
    (r"/genomics/prevalence-by-position", PrevalenceByAAPositionHandler),
    (r"/genomics/lineage-by-country-most-recent", CumulativeGlobalPrevalenceHandler),
    (r"/genomics/lineage-by-division-most-recent", CumulativePrevalenceByCountryHandler),
    (r"/genomics/lineage-by-county-most-recent", CumulativePrevalenceByDivisionHandler),
    (r"/genomics/most-recent-collection-date", MostRecentCollectionDateGlobalHandler),
    (r"/genomics/most-recent-collection-date-by-country", MostRecentCollectionDateByCountryHandler),
    (r"/genomics/most-recent-collection-date-by-division", MostRecentCollectionDateByDivisionHandler),
    (r"/genomics/most-recent-collection-date-by-county", MostRecentCollectionDateByCountyHandler),
    (r"/genomics/most-recent-submission-date", MostRecentSubmissionDateGlobalHandler),
    (r"/genomics/most-recent-submission-date-by-country", MostRecentSubmissionDateByCountryHandler),
    (r"/genomics/most-recent-submission-date-by-division", MostRecentSubmissionDateByDivisionHandler),
    (r"/genomics/most-recent-submission-date-by-county", MostRecentSubmissionDateByCountyHandler),
    (r"/genomics/mutation-details", MutationDetailsHandler),
    (r"/genomics/mutations-by-lineage", MutationsByLineage),
    (r"/genomics/lineage-mutations", LineageMutationsHandler),
    (r"/genomics/collection-submission", SubmissionLagHandler),
    (r"/genomics/lineage", LineageHandler),
    (r"/genomics/location", LocationHandler),
    (r"/genomics/mutations", MutationHandler),
    (r"/genomics/metadata", MetadataHandler)
]
