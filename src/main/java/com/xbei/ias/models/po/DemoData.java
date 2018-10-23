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
public class DemoData  extends BaseModel{

	private static final long serialVersionUID = 2738015830364794366L;
	
	@Id
	private Long id;
	private String name;
	private String top1;
	private String top2;
	private String top3;
	private String top4;
	private String top5;
	private String top6;
	private String top7;
	private String top8;
	private String top9;
	private String top10;
	private String top11;
	private String top12;
}
