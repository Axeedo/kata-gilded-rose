from helpers import persist, get_output
import gilded_rose

persist(get_output(gilded_rose.main), "golden-master/expected-output.txt")
