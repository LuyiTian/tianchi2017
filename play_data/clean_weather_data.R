# download city_weather and put it into dataset
setwd(paste(base_path, 'dataset', sep = ''))
# e.g. setwd('/Users/bianbeilei/tianchi2017/dataset/')

# download city_pinyin.txt and put it into dataset
# e.g. city_name <- read.table(file = '/Users/bianbeilei/tianchi2017/dataset/city_pinyin.txt')

all <- list.files('city_weather')
dir <- paste('./city_weather/', all, sep = '')

shop_info <- read.csv(file = './shop_info.txt', header = F, sep = ',')
date <- seq(from = as.Date('2015/7/1'), to = as.Date('2016/11/30'), by = 1)
shop_weather <- data.frame(matrix(NA, nrow = nrow(shop_info), ncol = length(date) + 1))

shop_weather[, 1] <- shop_info[, 2]
colnames(shop_weather) <- c('city', as.character(date))


for(i in 1:nrow(shop_info)) {
  m <- which(shop_info[i, 2] == city[, 1])
  weather_data <- read.csv(file = dir[which(city[m, 2] == all)], header = F, sep = ',')
  if(nrow(weather_data) < length(date)) {
    a <- match(weather_data[, 1], as.character(date))
    miss <- c(1:length(date))[-a]
    newrow <- rep(NA, 6)
    weather_data <- rbind(weather_data[1:(miss - 1), ], newrow, weather_data[-(1:(miss - 1)), ])
  }
  shop_weather[i, 2:ncol(shop_weather)] <- weather_data[, 4]
  rm(weather_data)
}

# fix a bug for simao
simao_new <- data.frame(matrix(NA, length(date), 6))
for(i in 1:nrow(simao)) {
  if(length(strsplit(as.character(simao[i, 1]), split = ',')[[1]]) == 4) {
    simao_new[i, ] <- c(strsplit(as.character(simao[i, 1]), split = ',')[[1]], NA, NA)
  } else if(length(strsplit(as.character(simao[i, 1]), split = ',')[[1]]) == 5) {
    simao_new[i, ] <- c(strsplit(as.character(simao[i, 1]), split = ',')[[1]], NA)
  } else {
    simao_new[i, ] <- strsplit(as.character(simao[i, 1]), split = ',')[[1]]
  }
}
# translate Chinese to pinyin
# read the weather data
weather <- read.csv(file = '', sep = ',')
# dataframe -> character
weather <- sapply(weather[, -(1:2)], as.character)
weather <- matrix(weather, 1, 2000 * 518)
# replace
weather <- sub('转', '~', weather)
final <- unique(weather)
weather_pinyin <- rep(NA, 2000 * 518)
for(i in 1:length(final)) {
  choose <- which(weather == final[i, 1])
  weather_pinyin[choose] <- final[i, 2]
}

# read citypinyin
city_pinyin <- rep(NA, 2000)
for(i in 1:nrow(city)) {
  choose <- which(city == citypinyin[i, 1])
  city_pinyin[choose] <- citypinyin[i, 2]
}