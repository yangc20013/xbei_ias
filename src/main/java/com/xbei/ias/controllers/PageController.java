package com.xbei.ias.controllers;

import org.springframework.stereotype.Controller;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

@Controller
public class PageController {
	
	@RequestMapping(value = "/", method = { RequestMethod.GET })
	public String index(ModelMap modelMap) {
		System.out.println("aaaaa");
		return "index";
	}
}
