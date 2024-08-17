import os
import json
from langchain_community.utilities import SearxSearchWrapper
from utils.helper_functions import load_config
from states.state import AgentGraphState

load_config(os.path.join(os.path.dirname(__file__), '..', 'config', 'config.yaml'))
searxng_search = SearxSearchWrapper(searx_host=os.environ['SEARXNG_URL'])

def format_results(organic_results):
        result_strings = []
        for result in organic_results:
            title = result.get('title', 'No Title')
            link = result.get('link', '#')
            snippet = result.get('snippet', 'No snippet available.')
            result_strings.append(f"Title: {title}\nLink: {link}\nSnippet: {snippet}\n---")
        
        return '\n'.join(result_strings)

def get_searxng(state:AgentGraphState, plan):
    plan_data = plan().content
    plan_data = json.loads(plan_data)
    search = plan_data.get("search_term")

    results = searxng_search.results(search, num_results=15)
    state = {**state, "search_response": format_results(results)}
    return state