from datetime import datetime
import pytz

def updateEntryPayload(error, cnt):
    return {
            "properties": {
                "Error": {
                    "id": "ErR0r",
                    "type": "rich_text",
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": error
                            }
                        }
                    ]
                },
                "Count": {
                    "number": cnt + 1
                },
                "Last Seen": {
                    "id": "LaSt",
                    "type": "date",
                    "date": {
                        "start": datetime.now(pytz.timezone('US/Eastern')).isoformat(),
                    }
                },
                "Status": {
                    "id": "StAtUs",
                    "type": "select",
                    "select": {
                        "name": "Not Resolved"
                    }
                }
            }
        }
    
def createEntryPayload(dbid, error, filename):
    return {
            "parent": {
                "database_id": dbid
            },
            "properties": {
                "Error": {
                    "id": "ErR0r",
                    "type": "rich_text",
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": error
                            }
                        }
                    ]
                },
                "File": {
                    "id": "FiLe",
                    "type": "rich_text",
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": filename.strip()
                            }
                        }
                    ]
                },
                "Count": {
                    "id": "CoUnT",
                    "type": "number",
                    "number": 1
                },
                "Last Seen": {
                    "id": "LaSt",
                    "type": "date",
                    "date": {
                        "start": datetime.now(pytz.timezone('US/Eastern')).isoformat(),
                    }
                },
                "Status": {
                    "id": "StAtUs",
                    "type": "select",
                    "select": {
                        "name": "Not Resolved"
                    }
                }
            }
        }