
"""
public class Animal {
    public String type;
    public Animal(String t) {
        this.type = t;
    }
}
"""


class Animal:
    type: str

    # constructor
    def __init__(self, t: str):
        self.type = t