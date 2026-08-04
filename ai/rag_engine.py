from ai.retriever import Retriever
from ai.prompt_builder import build_rag_prompt
from ai.ai_engine import generate_summary


class RAGEngine:

    def __init__(self):

        self.retriever = Retriever()

    # ==================================================
    # Private Method
    # ==================================================

    def _retrieve_context(self, question):
        """
        Retrieve the most relevant SOP from ChromaDB.
        """

        results = self.retriever.search(question)

        context = results["documents"][0][0]

        return context

    # ==================================================
    # Offline SOP Search
    # ==================================================

    def search_sop(self, question):
        """
        Return only the retrieved SOP.
        """

        context = self._retrieve_context(question)

        return {
            "success": True,
            "mode": "offline",
            "question": question,
            "answer": None,
            "context": context,
            "message": None
        }

    # ==================================================
    # AI Enhanced Explanation
    # ==================================================

    def ai_explain(self, question):
        """
        Retrieve SOP and generate AI explanation.
        """

        context = self._retrieve_context(question)

        prompt = build_rag_prompt(
            question,
            context
        )

        try:

            answer = generate_summary(prompt)

            return {
                "success": True,
                "mode": "ai",
                "question": question,
                "answer": answer,
                "context": context,
                "message": None
            }

        except Exception as e:

            return {
                "success": False,
                "mode": "offline",
                "question": question,
                "answer": None,
                "context": context,
                "message": str(e)
            }