package com.xbei.ias.models.po;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;

import com.xbei.ias.models.BaseModel;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Setter
@Getter
@AllArgsConstructor
@NoArgsConstructor
@Entity
public class FilterStock extends BaseModel{
	private static final long serialVersionUID = -4855563695433810208L;
	
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	private Long id;
	
	private String code;//股票代码
	private String date;//天日期
	private String daily;//日换手率
	private String weekDay;//周日期
	private String weekly;//周换手率
	
}
