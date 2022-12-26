"""
objetivo  contar la cantidad de palabras en un texto o en la variable dada

1. separando el texto por espacios
2. contando las palabras despues de la separacion 




def n_palabras(texto):
    return len(texto)
"""
texto = " * Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque finibus, enim eget ultrices auctor, odio elit ornare nisl, ac molestie metus lorem quis libero. Phasellus ac ante tristique, molestie sapien quis, placerat ante. Phasellus placerat ligula sed augue euismod, eu placerat nulla volutpat. Etiam ut sem non lectus iaculis cursus commodo quis est. Proin finibus eleifend porttitor. Cras blandit nulla a purus ullamcorper, et porta felis tincidunt. Donec eget eros arcu. Maecenas rutrum nunc eu urna commodo, non pellentesque ligula porttitor. Aenean eu quam at ipsum fringilla condimentum euismod quis tellus. * \
Sed vel erat quis libero ornare aliquet. Proin vel turpis mattis, elementum massa nec, lacinia nulla. Cras tincidunt sapien ac dictum elementum. Sed imperdiet massa sagittis metus mollis, non convallis eros posuere. Maecenas sit amet erat vel lorem ultrices luctus in fermentum tellus. Nullam vestibulum at arcu et consectetur. Vestibulum hendrerit nulla non blandit posuere. Donec sit amet sem ultrices odio pretium tempus. Maecenas sit amet posuere turpis. Nam efficitur efficitur interdum. In eu semper nulla. Phasellus posuere nisl nulla, ac tempor odio fermentum quis. Vestibulum non orci eget nisl faucibus sodales eget ut ante. Maecenas ultrices velit eu libero tincidunt, semper imperdiet ante vulputate. * \
Nam mattis, sem ut ullamcorper lobortis, nulla mi sollicitudin dolor, vel suscipit nibh mi at arcu. Sed ex urna, mollis id quam ac, fringilla faucibus justo. Maecenas imperdiet neque vitae luctus volutpat. Duis eu erat urna. Integer scelerisque, massa quis pretium fermentum, risus risus porttitor lorem, sed tempor massa odio at dolor. Morbi fringilla ultrices dolor a convallis. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Quisque et risus a tortor porttitor ornare. * \
Duis felis ante, sodales ac auctor posuere, mollis vel erat. Aliquam iaculis sagittis sollicitudin. Donec pretium felis id dui mollis euismod. Sed vitae eleifend eros. Sed finibus turpis et nunc vehicula posuere at ac risus. Vestibulum leo magna, pharetra ac accumsan vitae, efficitur et neque. Praesent non egestas ligula, eu vestibulum ligula. * \
In vitae tempus metus. Morbi euismod sapien eu diam congue, quis viverra mauris cursus. Proin risus neque, venenatis quis ornare vel, egestas eget mauris. Nullam ultricies nunc sit amet mi luctus commodo. Ut convallis pretium justo et ultrices. Aenean molestie metus non est elementum, lobortis elementum sem scelerisque. Maecenas arcu ligula, mollis in ipsum quis, euismod dictum erat. Morbi sagittis sagittis ultricies. Pellentesque faucibus risus vitae arcu dapibus, ac pretium libero varius. * \
Nulla ut nunc sollicitudin nibh cursus rutrum. Nullam justo lacus, vehicula eu dolor quis, feugiat viverra lorem. Sed nec tempus turpis, nec maximus orci. Proin dictum in sem eu lobortis. Quisque viverra sem nisi, id molestie dolor laoreet vitae. Phasellus interdum, felis in fermentum aliquam, justo mauris sagittis mi, id placerat purus libero ac magna. Ut dignissim suscipit lorem id molestie. * \
Aenean molestie et diam vitae commodo. Nam aliquet lectus ac neque fermentum fringilla. Pellentesque in pharetra diam, at sodales risus. Pellentesque blandit erat felis, eu tincidunt neque consequat in. Phasellus convallis, metus ac facilisis porta, augue purus blandit risus, vitae vestibulum leo massa a sapien. Fusce in tellus in ex suscipit tincidunt vel nec augue. Fusce turpis nunc, egestas vitae sem nec, tempus iaculis ante. Nunc felis urna, aliquet ut enim vitae, accumsan efficitur urna. Aenean feugiat ut dolor id tincidunt. Pellentesque tristique dolor ut consectetur congue. Praesent ultrices semper purus, eget tempor augue pretium sit amet.* \
Fusce erat est, dictum non viverra sed, mollis sed orci. Maecenas quis lorem commodo est viverra maximus sed sed urna. Sed eget ex mi. Proin cursus mollis est, nec viverra mi sollicitudin sed. Duis mauris libero, vulputate eget risus a, mattis aliquet nunc. Phasellus fringilla egestas consectetur. Praesent vehicula ex diam, quis mattis risus feugiat sit amet. Vivamus nibh turpis, mollis nec sapien ut, venenatis imperdiet ipsum. In non porta magna.* \
Sed commodo odio ullamcorper nisi maximus pretium. Integer nec ante nec orci feugiat posuere vitae sed lectus. Proin ac consectetur arcu. Ut est risus, tristique ac dignissim non, varius id urna. In nec turpis eu tellus congue consequat sed sit amet ipsum. Etiam ac dui mi. Sed interdum mi at posuere hendrerit. Pellentesque nibh orci, bibendum eu scelerisque eu, mattis sed arcu. Vestibulum viverra rutrum ex et vehicula. * \
Curabitur finibus, ex vel aliquet sollicitudin, nisl nibh vulputate magna, quis molestie magna nisl in mi. Vestibulum volutpat nisi at venenatis maximus. Vestibulum arcu libero, porta vitae mauris id, tincidunt suscipit tellus. Donec lorem ante, dignissim ut consectetur sit amet, dapibus condimentum magna. Curabitur ultrices eu lacus ut aliquet. Praesent euismod eros iaculis dui cursus fermentum. Aliquam volutpat purus varius est posuere molestie. Duis non est vehicula, bibendum lorem eget, aliquam odio. Vivamus dictum condimentum tempor. Fusce ullamcorper ornare massa, luctus gravida tellus placerat vel. Aenean suscipit elit nunc, nec dapibus velit vehicula commodo. Suspendisse potenti. Maecenas pellentesque venenatis dui, feugiat malesuada lectus sollicitudin at. * "

"""
longitud = n_palabras(texto)

lista_de_palabras=texto.split(" ")

print("la longitud del texto es", longitud)
print(len(lista_de_palabras))


def cont_lineas(texto):
    return texto.splitlines()

"""

lineas = texto.split(" * ")

nlin = len(lineas)
print(nlin)





