import sys
sys.path.append('/home/marco/PycharmProjects/coronavirus/')
import plot.graphics as graphics


graphics.axis('nuovi_positivi', 'Casi Giornalieri')
graphics.axis('deceduti', 'Decessi Giornalieri')
graphics.axis('terapia_intensiva', 'Terapie Intensive')
