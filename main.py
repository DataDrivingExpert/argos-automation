from pathlib import Path
import sys

from smp_extractor import run as extract_run
from concat import exec as transform_exec
from updater import exec as load_exec


def main() -> None:
	print("[ETL] Inicio del proceso")

	# Fase: Extract
	print("[ETL][Extract] Ejecutando extracción desde SMP...")
	try:
		ok = extract_run()
		if not ok:
			raise RuntimeError("Extracción no reportó finalización exitosa")
		print("[ETL][Extract] Extracción finalizada correctamente")
	except Exception as e:
		print(f"[ETL][Extract] Error: {e}")
		sys.exit(1)

	# Fase: Transform
	print("[ETL][Transform] Consolidando archivos XLSX en CSV...")
	try:
		out_path = transform_exec(out_filename="output")
		if not Path(out_path).exists():
			raise RuntimeError("No se generó el archivo de salida de transformación")
		print(f"[ETL][Transform] Transformación OK: {out_path}")
	except Exception as e:
		print(f"[ETL][Transform] Error: {e}")
		sys.exit(1)

	# Fase: Load
	print("[ETL][Load] Actualizando hojas de cálculo en Google Sheets...")
	try:
		loaded = load_exec()
		if loaded is False:
			raise RuntimeError("Carga no reportó finalización exitosa")
		print("[ETL][Load] Carga finalizada correctamente")
	except Exception as e:
		print(f"[ETL][Load] Error: {e}")
		sys.exit(1)

	print("[ETL] Proceso completado")


if __name__ == "__main__":
	main()
