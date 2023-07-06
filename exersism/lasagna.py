# bake lasagna

EXPECTED_BAKE_TIME = 40
TIME_TO_PREPARE_LAYERS = 2

def bake_time_remanin(time):
    return EXPECTED_BAKE_TIME - time

def preparation_time_in_minutes(layers):
    return TIME_TO_PREPARE_LAYERS * layers

def elapsed_time_in_minutes(layers, elapsed_time):
    """Calculate the elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.

    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.
    """
    return (TIME_TO_PREPARE_LAYERS * layers) + (EXPECTED_BAKE_TIME - elapsed_time)


elapsed_time_in_minutes(3, 20)