class IdGenerator:
    id = {}

    @staticmethod
    def generate_id(model: str):
        IdGenerator.id[model] = 1 + IdGenerator.id.get(model, 0)
        return IdGenerator.id
