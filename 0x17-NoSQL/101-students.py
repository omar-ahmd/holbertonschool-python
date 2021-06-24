#!/usr/bin/env python3
"""pumongo aggregate"""


def top_students(mongo_collection):
    """Return students sorted based on their average score"""
    return mongo_collection.aggregate([
        {
            "$project":
                {
                    "name": "$name",
                    "averageScore": {"$avg": "$topics.score"}
                }
        },
        {
            "$sort":
                {
                    "averageScore": -1
                }
        }
    ])
