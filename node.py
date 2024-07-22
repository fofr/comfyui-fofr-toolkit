class Incrementer:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "current_index": (
                    "INT",
                    {
                        "default": 0,
                        "min": 0,
                        "max": 0xFFFFFFFFFFFFFFFF,
                        "control_after_generate": True,
                    },
                ),
            },
            "optional": {
                "max": (
                    "INT",
                    {"default": 10, "min": 0, "max": 0xFFFFFFFFFFFFFFFF},
                ),
            },
        }

    RETURN_TYPES = ("INT",)
    FUNCTION = "increment"
    CATEGORY = "fofr-toolkit"

    def increment(self, current_index, max=0):
        if max == 0:
            return (current_index,)

        return (current_index % (max + 1),)


NODE_CLASS_MAPPINGS = {
    "Incrementer 🪴": Incrementer,
}
