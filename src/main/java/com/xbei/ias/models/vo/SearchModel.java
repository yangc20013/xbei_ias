package com.xbei.ias.models.vo;

import java.util.List;

import org.springframework.data.domain.Sort.Direction;

import com.xbei.ias.models.BaseModel;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Setter
@Getter
@AllArgsConstructor
@NoArgsConstructor
public class SearchModel extends BaseModel {

	private static final long serialVersionUID = 6710048320883104994L;
	
	private int pageSize;
	private int pageNum;
	private Direction order;
	private String sortColumn;
	
	private List<String> stocks;
	
	private float dayRate;
	private float weekRate;
}
