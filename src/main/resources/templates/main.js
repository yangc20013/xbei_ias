var stock = {
	json: {
		title: '数据报表',
		subtitle: null,
		xAxis: {
			categories: ["20190901", "20190902"]
		},
		yAxis: {
			title: {
				text: "价格(元)"
			},
			plotLines: [{
				value: 0,
				width: 1,
				color: '#f4f4f4'
			}]
		},
		tooltip: {
			valueSuffix: ' ￥'
		},
		legend: {
			layout: 'vertical',
			align: 'right',
			verticalAlign: 'middle',
			borderWidth: 0
		},
		series: [{
			name: "股票名称",
			data: [1.00, 2.00]
		}]
	},
	init: function () {
		var set = {
			    enableFiltering: true,//搜尋
			    includeSelectAllOption: true,//全選
			    nonSelectedText: '全部',//沒有值的時候button顯示值
			    nSelectedText: '个被选中',//有n個值的時候顯示n個被選中
			    allSelectedText: '全选',//所有被選中的時候 全選（n）
			    buttonWidth: '220px',//button寬度
			    numberDisplayed: 1000,//當超過1000個標籤的時候顯示n個被選中
			    selectAllText: '全选',
			    templates: {
			        button: '<button type="button" class="multiselect dropdown-toggle" data-toggle="dropdown" style="text-align:center;background-color: #ffffff;border: 1px solid #e5e5e5;"><span class="multiselect-selected-text"></span></button>',
			        ul: '<ul class="multiselect-container dropdown-menu" style="max-height: 200px;overflow-x: hidden;overflow-y: auto;-webkit-tap-highlight-color: rgba(0,0,0,0);"></ul>',
			        filter: '<li class="multiselect-item multiselect-filter"><div class="input-group"><span class="input-group-addon"><i class="glyphicon glyphicon-search"></i></span><input class="form-control multiselect-search" type="text"></div></li>',
			        filterClearBtn: '<span class="input-group-btn"></span>',
			        li: '<li><a tabindex="0"><label style="margin-left:20%;"></label></a></li>',
			        divider: '<li class="multiselect-item divider"></li>',
			        liGroup: '<li class="multiselect-item multiselect-group"><label></label></li>'
			    }
			};
		$("#stocks").multiselect(set);
		
		$.get("/stock/stockList", function (data, status) {
			if (Array.isArray(data)) {
				var options = [];
				$.each(data, function (r, row) {
		            var obj = new Object();
		            obj.label = row.name;
		            obj.title = row.name;
		            obj.value = row.code;
		            options.push(obj);
		        });
				$("#stocks").multiselect('dataprovider',options)
			}
		});
		 $("#btn_search").click(function() {
		 	stock.search();
		 });
	},
	search: function () {
		var _this = this;
		
		var getStockSelected = function () {
		    var selectValueStr = [];
		    $("#stocks").each(function () {
		        selectValueStr.push($(this).val());
		    });
		    return selectValueStr;
		}
		$.get("/stock/hotStockDetail", {"code": getStockSelected().join()}, function (data, status){
			if(data){
				_this.json.xAxis.categories = data.categories;
				_this.json.series = data.series;
				
				$('#stock_panel').highcharts(_this.json);
			}
		});
		
	},
//	test: function () {
//		var title = {
//			text: '月平均气温'
//		};
//		var subtitle = {
//			text: 'Source: runoob.com'
//		};
//		var xAxis = {
//			categories: ['一月', '二月', '三月', '四月', '五月', '六月', '七月', '八月', '九月', '十月', '十一月', '十二月']
//		};
//		var yAxis = {
//			title: {
//				text: 'Temperature (\xB0C)'
//			},
//			plotLines: [{
//				value: 0,
//				width: 1,
//				color: '#808080'
//			}]
//		};
//
//		var tooltip = {
//			valueSuffix: '\xB0C'
//		}
//
//		var legend = {
//			layout: 'vertical',
//			align: 'right',
//			verticalAlign: 'middle',
//			borderWidth: 0
//		};
//
//		var series = [
//			{
//				name: 'Tokyo',
//				data: [7.0, 6.9, 9.5, 14.5, 18.2, 21.5, 25.2, 26.5, 23.3,
//					18.3, 13.9, 9.6]
//			},
//			{
//				name: 'New York',
//				data: [-0.2, 0.8, 5.7, 11.3, 17.0, 22.0, 24.8, 24.1, 20.1,
//					14.1, 8.6, 2.5]
//			},
//			{
//				name: 'Berlin',
//				data: [-0.9, 0.6, 3.5, 8.4, 13.5, 17.0, 18.6, 17.9, 14.3,
//					9.0, 3.9, 1.0]
//			},
//			{
//				name: 'London',
//				data: [3.9, 4.2, 5.7, 8.5, 11.9, 15.2, 17.0, 16.6, 14.2,
//					10.3, 6.6, 4.8]
//			}];
//
//		var json = {};
//
//		json.title = title;
//		json.subtitle = subtitle;
//		json.xAxis = xAxis;
//		json.yAxis = yAxis;
//		json.tooltip = tooltip;
//		json.legend = legend;
//		json.series = series;
//
//		$('#stock_panel').highcharts(json);
//	},
	reload: function () {
		console.log(stock.json);
		$('#stock_panel').highcharts(stock.json);
	}
};

$(function () {
	stock.init();
});