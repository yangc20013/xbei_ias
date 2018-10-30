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
public class Dict extends BaseModel{
	private static final long serialVersionUID = 7456352809325902226L;
	
	@Id
	private String name;
	private String value;
	private String description;

}
