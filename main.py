import gui_package.gui
import recommend_system_package.contented_base
import recommend_system_package.collab_filtering
import function_package.read_data_function

if __name__ == "__main__":
    data_matrix = function_package.read_data_function.get_dataframe_ratings_base('dataset/ml-100k/ub.base')
    cf_rs = recommend_system_package.collab_filtering.CF(data_matrix, k=2, uuCF=1)
    cf_rs.fit()

    cb_rs = recommend_system_package.contented_base.CB('dataset/movilens_csv/movies.csv')
    cb_rs.fit()

    list_name_movie = function_package.read_data_function.get_name_movie('dataset/ml-100k/u.item')
    list_year_movie = function_package.read_data_function.get_year_movie('dataset/ml-100k/u.item')
    gui_package.gui.main(cf_rs, cb_rs, list_name_movie, list_year_movie)

