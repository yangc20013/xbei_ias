package com.xbei.ias.controllers;

import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.xbei.ias.services.StockService;

@RestController
@RequestMapping(value = "/stock")
public class StockController {
	
	@Autowired
	private StockService stockService;
	
	@RequestMapping(value = "/stockList", method = RequestMethod.GET)
	public ResponseEntity<List<Map<String,Object>>> stockList() {
		return new ResponseEntity<>(stockService.findHotList(),HttpStatus.OK);
	}
	
	@RequestMapping(value = "/hotStockDetail", method = RequestMethod.GET)
	public ResponseEntity<Map<String,Object>> hotStockDetail(@RequestParam(required=false) List<String> code) {
		Map<String,Object> result = stockService.findHotStockDetail(code);
		return new ResponseEntity<>(result, HttpStatus.OK);
	}
}
