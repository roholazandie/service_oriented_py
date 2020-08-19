from services.service import Service
import wikipedia, re

class WikipediaService(Service):

    def __init__(self, config=None, api=None):
        super().__init__(config)

    def clean_summary(self, summary):
        # NOTE: Often wikipedia articles will have a listen plug-in in the summary.
        #       We need to make sure to get rid of extraneous characters
        #       so Ryan sounds natural, hence the cleaning.
        # print("BEFORE CLEANING")
        # print("summary: {}".format(summary))
        summary = summary.replace("(listen);", "")
        summary = summary.replace("(listen),", "")
        summary = summary.replace("(listen)", "")
        summary = summary.replace("IPA: ", "")
        summary = summary.replace("( )", "")

        summary.encode("ascii", errors="ignore")
        summary = re.sub('\[.*\]', '', summary)
        return summary

    def ask_wikipedia(self, question, sentences=2, chars=0, auto_suggest=True, redirect=False):
        try:
            return wikipedia.summary(question, sentences, chars, auto_suggest, redirect)
        except Exception as ex:
            print("General error querying Wikipedia for your question [%s], Exception - [%s]", question, ex)
        return "Sorry, but I couldn't find anything on Wikipedia for your question about, " + question

