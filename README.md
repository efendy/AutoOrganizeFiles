input:
	directory path

validate:
	exit the script if directory path does not exist

logic:
	while(True)
		iterate files in the directory path
			extract the extension
			if subdirectory name is extension does not exist
				create a subdirectory name
			put file in the subdirectory
		sleep for 5 seconds

optimize:
	start -d directory path
	end -d directory path
	list
	create .efendy directory at home
	create {scriptname}.{process_id} contain directory path

