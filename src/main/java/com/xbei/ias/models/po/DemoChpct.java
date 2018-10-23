package com.xbei.ias.models.po;

import java.util.Calendar;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;
import javax.persistence.Temporal;
import javax.persistence.TemporalType;

import com.fasterxml.jackson.annotation.JsonFormat;
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
@Table(name = "chpct")
public class DemoChpct extends BaseModel{
	
	private static final long serialVersionUID = 7668178612949130186L;
	
	@Id
	private Long id;
	
	@Temporal(TemporalType.TIMESTAMP)
	@JsonFormat(pattern="yyyy/MM/dd")
	private Calendar tradeDate;
	
	@Column(name="chpct_diff_hs300")
	private Double chpctDiffHs300;
	@Column(name="volatility20_HS300")
	private Double volatility20Hs300;
	
	@Column(name="tv20_chpct_HS300")
	private Double tv20ChpctHs300;
	
	@Column(name="chpct_diff_ZZ500")
	private Double chpctDiffZz500;
	
	@Column(name="volatility20_ZZ500")
	private Double volatility20Zz500;
	
	@Column(name="tv20_chpct_ZZ500")
	private Double tv20ChpctZz500;
	private Double baselineMae;
	private Double staticMae;
	private Double improved;
	

}
