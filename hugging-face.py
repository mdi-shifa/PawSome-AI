from huggingface_hub import HfApi
api = HfApi(token="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")

api.upload_folder(
    folder_path="C:/Users/$ ASUS $/Desktop/Deployment/faiss_index",
    repo_id="Shifaa/PawSome-AI-V2",
    repo_type="space",
)