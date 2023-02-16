
class MostRecentDateHandler(BaseHandler):
    field = "date_collected"

    @gen.coroutine
    def _get(self):
        query_pangolin_lineage = self.get_argument("pangolin_lineage", None)
        query_location = self.get_argument("location_id", None)
        query_mutations = self.get_argument("mutations", None)
        query_mutations = query_mutations.split(",") if query_mutations is not None else []
        query = {
            "size": 0,
            "query": {},
            "aggs": {
                "date_collected": {
                    "terms": {
                        "field": self.field,
                        "size": 10000
                    }
                }
            }
        }
        query_pangolin_lineage = query_pangolin_lineage.split(",") if query_pangolin_lineage is not None else []
        query_obj = create_nested_mutation_query(lineages = query_pangolin_lineage, mutations = query_mutations, location_id = query_location)
        query["query"] = query_obj
        resp = yield self.asynchronous_fetch(query)
        #print(resp)
        path_to_results = ["aggregations", "date_collected", "buckets"]
        buckets = resp
        for i in path_to_results:
            buckets = buckets[i]
        if len(buckets) == 0:
            return {"success": True, "results": []}
        flattened_response = []
        for i in buckets:
            if len(i["key"].split("-")) == 1 or "XX" in i["key"]:
                continue
            flattened_response.append({
                "date": i["key"],
                "date_count": i["doc_count"]
            })
        df_response = (
            pd.DataFrame(flattened_response)
            .assign(
                date = lambda x: pd.to_datetime(x["date"], format="%Y-%m-%d"),
                date_count = lambda x: x["date_count"].astype(int)
            )
            .sort_values("date")
        )
        df_response = df_response.iloc[-1]
        df_response.loc["date"] = df_response["date"].strftime("%Y-%m-%d")
        df_response.loc["date_count"] = int(df_response["date_count"])
        dict_response = df_response.to_dict()
        resp = {"success": True, "results": dict_response}
        return resp


class MostRecentCollectionDateHandler(MostRecentDateHandler):
    field = "date_collected"

class MostRecentSubmissionDateHandler(MostRecentDateHandler):
    field = "date_submitted"
