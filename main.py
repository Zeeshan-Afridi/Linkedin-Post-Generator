from agents import (
    generate_approved_hook,
    generate_approved_post
)


# ==================================================
# USER INPUT
# ==================================================

topic = input("Enter LinkedIn topic: ")


# ==================================================
# STEP 1 — GENERATE HOOK
# ==================================================

hook = generate_approved_hook(topic)


# ==================================================
# STEP 2 — GENERATE POST
# ==================================================

final_post = generate_approved_post(topic, hook)


# ==================================================
# FINAL OUTPUT
# ==================================================

print("\n==============================")
print("FINAL LINKEDIN POST")
print("==============================\n")

print(final_post)