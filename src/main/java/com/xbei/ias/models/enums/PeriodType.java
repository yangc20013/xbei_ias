package com.xbei.ias.models.enums;

public enum PeriodType {
	DAY(0,"d"),WEEK(1,"w"),MONTH(2,"m");
	
	private int type;
	private String name;
	
	private PeriodType(int type,String name) {
		this.type = type;
		this.name = name;
	}
	
	public int getValue() {
		return this.type;
	}
	
	public String getName() {
		return this.name;
	}
}
