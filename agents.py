from config import llm

from prompts import (
    hook_prompt,
    hook_review_prompt,
    body_prompt,
    review_prompt
)


# ==================================================
# CREATE CHAINS
# ==================================================

hook_chain = hook_prompt | llm
hook_review_chain = hook_review_prompt | llm
body_chain = body_prompt | llm
review_chain = review_prompt | llm


# ==================================================
# HOOK GENERATION LOOP
# ==================================================

def generate_approved_hook(topic, max_retries=3):

    feedback = "No feedback yet"

    for attempt in range(max_retries):

        print(f"\nGenerating Hook Attempt {attempt + 1}...")

        hook_response = hook_chain.invoke({
            "topic": topic,
            "feedback": feedback
        })

        hook = hook_response.content

        print("\nGenerated Hook:\n")
        print(hook)

        review_response = hook_review_chain.invoke({
            "hook": hook
        })

        review = review_response.content

        print("\nHook Review:\n")
        print(review)

        if "STATUS: APPROVED" in review:
            return hook

        feedback = review

    return hook


# ==================================================
# BODY GENERATION LOOP
# ==================================================

def generate_approved_post(topic, hook, max_retries=3):

    feedback = "No feedback yet"

    for attempt in range(max_retries):

        print(f"\nGenerating Post Attempt {attempt + 1}...")

        body_response = body_chain.invoke({
            "topic": topic,
            "hook": hook,
            "feedback": feedback
        })

        post = body_response.content

        print("\nGenerated Post:\n")
        print(post)

        review_response = review_chain.invoke({
            "post": post
        })

        review = review_response.content

        print("\nPost Review:\n")
        print(review)

        if "STATUS: APPROVED" in review:
            return post

        feedback = review

    return post