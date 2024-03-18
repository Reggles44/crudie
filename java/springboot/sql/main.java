package com.reggles;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.Param;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;


private class CrudieData {
	public long id;
	public String service_key;
	public int data;
}


public class CrudieApplication {
	public static void main(String[] args) {
		SpringApplication.run(CrudieAplication.class, args);

	}
	
	@PostMapping("/create")
	public  create()
}

