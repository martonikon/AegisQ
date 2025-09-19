from tasks.text_cleaner import clean_text
 
class TaskDispatcher:
    def dispatch(self, task_type, payload):
        if task_type == "clean_text":
            return clean_text(payload)
        raise ValueError(f"Unsupported task type: {task_type}")