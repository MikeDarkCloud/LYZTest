#查询可报读院校
	SELECT
        u.`unvs_id` as unvsId,
        u.`unvs_code` as unvsCode,
        u.`unvs_name` as unvsName,
        u.`recruit_type` as recruitType
        FROM
        bms.bd_university u
            LEFT JOIN bms.bd_unvs_profession bup
            ON u.`unvs_id` = bup.`unvs_id`
        where
              u.recruit_type = 1
                and bup.`pfsn_level` = 5
            and u.is_stop = '0'
            GROUP BY u.`unvs_id`
#修改
SELECT *FROM bms.bd_university WHERE unvs_id in ('158674219979815123','158674881863381415','152989436245450072','50','55')