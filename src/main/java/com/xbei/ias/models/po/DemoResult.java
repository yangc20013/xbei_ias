package com.xbei.ias.models.po;

import javax.persistence.Entity;
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
public class DemoResult extends BaseModel {
	private static final long serialVersionUID = -1613581525655646763L;
	
	@Id
	private Long id;
	private String code;
	private String name;
}
